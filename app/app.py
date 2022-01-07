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
        query = '{***REMOVED*** lang:en -is:retweet'.format(request.form['query'])

    max_results = 10
    tweets = search.returnSearchTweetList(query, max_results)

    return render_template('index.html', **locals())


@app.route('/retweet/<string:tweetId>/', methods=["GET", "POST"])
def reweet(tweetId):
    search.retweet(tweetId)

    return redirect(url_for('index'))





if __name__ == '__main__':
    client = tweet.getClient()
    client.create_tweet(poll_options=['Yes', 'No'], poll_duration_minutes=5, text='Is kaya toast delicious???')
    client.Poll()