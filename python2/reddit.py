import time
from datetime import datetime
import re
from config import CLIENT_ID, CLIENT_SECRET, USERNAME, PASSWORD, EMAIL
import praw
import ezgmail

# setting up seperate date and time variables
current_datetime = datetime.now()
current_date = current_datetime.strftime('%Y-%m-%d')
current_time = current_datetime.strftime('%H:%M:%S')

reddit = praw.Reddit(
    client_id=f"{CLIENT_ID}",
    client_secret=f"{CLIENT_SECRET}",
    password=f"{PASSWORD}",
    user_agent=f"just testing lol - /u/{USERNAME}",
    username=f"{USERNAME}")


subreddit = reddit.subreddit('hardwareswap')
keyword = 'z690'

# Initialize a flag to keep track of whether the keyword was found in the most recent batch of posts
keyword_found = False

# Loop through the most recent 100 posts in the subreddit
for post in subreddit.new(limit=200):
    # Extract text between [H] and [W]
    title_text = re.search(r'\[H\](.*?)\[W\]', post.title).group(1)

    # Check if the keyword is in the extracted text
    if keyword in title_text.strip():
        print(f'Found a post matching your keyword, "{keyword}". \n Here is the url: {post.url}')
        ezgmail.send(f'{EMAIL}', 'Post Found!', f'Found a post for your keyword, "{keyword}". Here is the link: {post.url} {current_datetime}.')
        keyword_found = True

# If the keyword was not found in the most recent batch of posts, print "not found" once
if not keyword_found:
    print("not found")

