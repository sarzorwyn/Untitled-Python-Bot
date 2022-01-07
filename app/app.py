import time

from flask import Flask, render_template, url_for, redirect, request
import config
import tweet
import connectFour
import random

TWITTER_MAX_POLL_OPTIONS = 4

def page_not_found(e):
    return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)

def createPollOptions(game):
    validMoves = game.get_valid_moves()
    while len(validMoves) > TWITTER_MAX_POLL_OPTIONS:
        index = random.randrange(0, len(validMoves) - 1)
        validMoves.pop(index)

    return validMoves
    #
    #
    # for move in validMoves:
    #     for i in range(1, 21):
    #         s = s.replace(chr(0x245f + i), str(i))
    #     return s.replace('\u24ea', '0')
    #     poll_options.append(move)


# Returns a list of dictionary. E.g.[{'position': 1, 'label': 'awesome', 'votes': 1***REMOVED***, {'position': 2, 'label': 'nice', 'votes': 0***REMOVED***]
def getPollDetails(tweetID):
    response = client.get_tweet(id=tweetID, expansions="attachments.poll_ids")
    return response.includes["polls"][0]["options"]

def getNextMove(poll):
    nextPosMoves = []
    maxVote = 0

    for d in poll:
        if maxVote < d["votes"]:
            nextPosMoves.clear()
            nextPosMoves.append(d["label"])
            maxVote = d["votes"]

        elif maxVote == d["votes"]:
            nextPosMoves.append(d["label"])

        print("Option: " + d["label"] + ", Votes: " + str(d["votes"]))

    return int(nextPosMoves[random.randrange(0, len(nextPosMoves) - 1)])  # Random for tiebreaker

def noVotes(poll):
    for d in poll:
        if d["votes"] != 0:
            return False
    return True


if __name__ == '__main__':
    client = tweet.getClient()
    game = connectFour.ConnectFour.new_game()
    while True:
        pollOptions = createPollOptions(game)
        pollID = client.create_tweet(poll_options=pollOptions, poll_duration_minutes=5, text=game.board_to_emoji())
        time.sleep(60)
        print(pollID.data['id'])
        tweetId = pollID.data['id']
        poll = getPollDetails(tweetId)
        if noVotes(poll):  # Restart game if no one votes
            game = connectFour.ConnectFour.new_game()
            continue
        if game.play_turn(getNextMove(poll)):
            game = connectFour.ConnectFour.new_game()
            client.create_tweet(text="Congrats whoever won")  # need to create function to output game board



    # client.Poll()
