import time

from flask import Flask, render_template, url_for, redirect, request
import config
import tweet


def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)



@app.route('/', methods=["GET", "POST"])
def index():

    query = 'Project Management lang:en -is:retweet'

    if request.method == 'POST':
        query = '{} lang:en -is:retweet'.format(request.form['query'])

    max_results = 10
    tweets = search.returnSearchTweetList(query, max_results)

    return render_template('index.html', **locals())


@app.route('/retweet/<string:tweetId>/', methods=["GET", "POST"])
def reweet(tweetId):
    search.retweet(tweetId)

    return redirect(url_for('index'))

# Returns a list of dictionary. E.g.[{'position': 1, 'label': 'awesome', 'votes': 1}, {'position': 2, 'label': 'nice', 'votes': 0}]
def getPollDetails(tweetID):
    response = client.get_tweet(id=tweetID, expansions="attachments.poll_ids")
    return response.includes["polls"][0]["options"]

if __name__ == '__main__':
    client = tweet.getClient()
    pollID = client.create_tweet(poll_options=['🍞', '🥐'], poll_duration_minutes=5, text='Toast?')
    # time.sleep(300)
    # print(pollID.data['id'])
    tweetId = pollID.data['id']
    poll = getPollDetails(tweetId)
    for d in poll:
        print("Option: " + d["label"] + ", Votes: " + str(d["votes"]))
    # client.Poll()