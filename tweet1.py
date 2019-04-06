from flask import Flask, render_template, request
import tweepy
consumer_key = "klc9lTZuJfxAalGGOIXFjTbhr"
consumer_secret = "gPhGZE1j6egZSXTkyw5p3mZdem2VhNb8aHxfCae7PtPggJKF8q"
access_token = "1112587571622637568-BR4xHHlqA7L0e58zp0bKB9U6I5AFfj"
access_token_secret = "GrcusxoUGerHchMsbmdTFRw6ZHbnCcI7NTa85GL2LjDLu"
app=Flask(__name__)
@app.route('/')
def index():
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)
  search=request.args.get('query')
  public_tweets = api.user_timeline(search,count=10)
  return render_template('ho.html', tweets=public_tweets)
if __name__=='__main__':
  app.run(debug=True)
   
