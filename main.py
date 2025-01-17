from bot_tweepy.bot_x import client,api
from bot_selenium.scrape import scrape_data
from generate_pdf.render_pdf import create_pdf
from transform_png import transform_pdf_to_png
from nlp_tweet import get_text



def bot_twitter():
    response = client.search_recent_tweets(query="@datascoutme")
    if response.data:
        for tweet in response.data:
            name,camp = get_text(tweet.text).values()
            obj = scrape_data(name,camp)
            create_pdf(obj)
            transform_pdf_to_png("scout.pdf")
            media_id = api.media_upload(filename="scout.png").media_id_string
            client.create_tweet(media_ids=[media_id],in_reply_to_tweet_id=tweet.id)
            
bot_twitter()
