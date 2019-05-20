import praw
import pandas as pd

    
def web_scrapper():
    my_client_id="YOUR_ID"
    my_client_secret="YOUR_SECRETE_KEY"
    user_agent="YOUR_APP_NAME"
    reddit = praw.Reddit(client_id=my_client_id, client_secret=my_client_secret, user_agent=user_agent)
    
    posts = []
    showerthoughts = reddit.subreddit('ShowerThoughts')
    for post in showerthoughts.hot(limit=10000):
        posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
    posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
    
    posts.to_csv("data.csv")


def random_thoughts():
    thoughts=pd.Series.from_csv("data.csv")
    thoughts=thoughts.sample()
       
    return thoughts.values[0]
