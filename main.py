import praw
import time
from google import genai
import config
from config import GEMINI_KEY, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET


class RedditBot:
    def __init__(self, client_id, client_secret, password, user_agent, username):
        client_id = f"{REDDIT_CLIENT_ID}"
        client_secret = f"{REDDIT_CLIENT_SECRET}"
        password = ""
        user_agent = ""
        username =  ""
        self.reddit = praw.Reddit(client_id = client_id, client_secret = client_secret, user_agent = user_agent)

    def get_headlines(self, subreddit, count = 10):
        headlines = []

        subreddit = "r/WorldNews"

        posts = self.reddit.subreddit(subreddit).hot(limit = count)

        for post in posts:
            headlines.append(post.title)

        return headlines

    def summarize_news(self, list_of_headlines):
        client = genai.Client(api_key=GEMINI_KEY)
        prompt = f"Here are the top news headlines from Reddit today. Explain and summarize in 2 - 3 sentences in the same order, split by '-----'.{list_of_headlines}"
        response = client.models.generate_content(model="gemini-3-flash-preview", contents=prompt)

        return response

    def print_headline_and_summarizedtxt(self, headlines, summarizedtxt):
        headlines_parts = headlines.split(",")
        summarizedtxt_parts = summarizedtxt.split("-----")
