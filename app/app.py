import time

from flask import Flask, render_template, url_for, redirect, request
import config
import tweet
import connectFour
import random

TWITTER_MAX_POLL_OPTIONS = 4
POLL_TIME = 5  # In minutes
ROUND_TIME = 300  # In seconds

def page_not_found(e):
    return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)

def createPollOptions(game):
    validMoves = game.get_valid_moves()
    while len(validMoves) > TWITTER_MAX_POLL_OPTIONS:
        index = random.randrange(0, len(validMoves))
        validMoves.pop(index)

    return validMoves


# Returns a list of dictionary. E.g.[{'position': 1, 'label': 'awesome', 'votes': 1}, {'position': 2, 'label': 'nice', 'votes': 0}]
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

    if len(nextPosMoves) == 1:
        return nextPosMoves[0]

    return nextPosMoves[random.randrange(0, len(nextPosMoves) - 1)]  # Random for tiebreaker

def noVotes(poll):
    for d in poll:
        #print(d["votes"])
        if d["votes"] != 0:
            return False
    return True

def sendWinnerTweet(client, winner):
    if winner == 1:
        winnerIcon = '🔴'  # red circle
    else:
        winnerIcon = '🔵'  # blue circle

    output = '🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊\n'
    output += 'The winner is ' + winnerIcon + '!\n'

    output += game.board_to_emoji()
    client.create_tweet(text=output)


if __name__ == '__main__':
    client = tweet.getClient()
    game = connectFour.ConnectFour.new_game()
    while True:
        pollOptions = createPollOptions(game)
        pollID = client.create_tweet(poll_options=pollOptions, poll_duration_minutes=POLL_TIME, text=game.board_to_emoji()) # 5mins is min duration
        time.sleep(ROUND_TIME)
        print(pollID.data['id'])
        tweetId = pollID.data['id']
        poll = getPollDetails(tweetId)
        # if noVotes(poll):  # Restart game if no one votes
        #     print("no votesesss!!OIJHDFIWHDI")
        #     game = connectFour.ConnectFour.new_game()
        #     continue
        if game.play_turn(getNextMove(poll)):
            sendWinnerTweet(client, game.get_active_player())  # need to create function to output game board
            game = connectFour.ConnectFour.new_game()



    # client.Poll()
