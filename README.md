# reddit-scraper
Data Collection from Reddit Subreddits
This script collects the latest 50–100 posts from specified Reddit subreddits and saves the data into an Excel file with a separate sheet for each subreddit.
Features
Fetches posts from these subreddits: AskReddit, todayilearned, technology, worldnews.
Retrieves all available post fields: title, author, upvote ratio, score, number of comments, full text, flair, post time, NSFW status, and other metadata.
Saves data into a single Excel file with 4 sheets, one per subreddit.
Requirements:
1) Python 3.7 or higher
2) Python libraries: praw, pandas, openpyxl.
(install with: pip install praw pandas openpyxl)
Setup:
1) Create a reddit app at https://www.reddit.com/prefs/apps/ to get your client_id and client_secret.
2) Replace the placeholders in the script with your credentials:
reddit = praw.Reddit(
    client_id="your client id",
    client_secret="your client secret",
    user_agent="Scraper 1.0 by u/your reddit username"
)
3) Optionally, modify the list of subreddits or number of posts (POST_LIMIT).
Usage:
Run the script with:
python reddit_scraper.py
After running, an Excel file named reddit_posts.xlsx will be created in the current directory containing the scraped data.
Customization:
To change which subreddits or how many posts to fetch, edit these variables at the top of the script:
SUBREDDITS = ["AskReddit", "todayilearned", "technology", "worldnews"]
POST_LIMIT = 100
If you have any questions or need help, feel free to ask!
