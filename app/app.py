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


# Returns a list of dictionary. E.g.[{'position': 1, 'label': 'awesome', 'votes': 1}, {'position': 2, 'label': 'nice', 'votes': 0}]
def getPollDetails(tweetID):
    response = client.get_tweet(id=tweetID, expansions="attachments.poll_ids")
    return response.includes["polls"][0]["options"]


if __name__ == '__main__':
    client = tweet.getClient()
    game = connectFour.ConnectFour.new_game()
    pollOptions = createPollOptions(game)

    pollID = client.create_tweet(poll_options=pollOptions[:4], poll_duration_minutes=5, text=game.board_to_emoji())
    # time.sleep(300)
    print(pollID.data['id'])
    tweetId = pollID.data['id']
    poll = getPollDetails(tweetId)
    for d in poll:
        print("Option: " + d["label"] + ", Votes: " + str(d["votes"]))
    # client.Poll()
