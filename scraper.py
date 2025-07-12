import praw
import pandas as pd
from datetime import datetime

#settings
SUBREDDITS = ["AskReddit", "todayilearned", "technology", "worldnews"]
POST_LIMIT = 100  #can change

#output filename
OUTPUT_EXCEL = "reddit_posts.xlsx"

#initializing reddit API (replace client_id and client_secret with your own (if needed))
user_agent = "Scraper 1.0 by u/your reddit username"
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent=user_agent
)

#dictionary for storing dataframes by subreddit
all_dfs = {}

#main subreddit cycle
for sub in SUBREDDITS:
    print(f"currently in r/{sub}...")
    rows = []
    subreddit = reddit.subreddit(sub)

    #receiving posts (new)
    for post in subreddit.new(limit=POST_LIMIT):

        #collect all available fields from the post into a dictionary
        data = {
            "subreddit": post.subreddit.display_name,
            "title": post.title,
            "author": str(post.author),
            "upvote_ratio": post.upvote_ratio,
            "score": post.score,
            "num_comments": post.num_comments,
            "selftext": post.selftext,
            "flair": post.link_flair_text or "",
            "created_utc": datetime.fromtimestamp(post.created_utc).replace(tzinfo=None),
            "nsfw": str(post.over_18),
            "permalink": f"https://reddit.com{post.permalink}",
            "url": post.url,
            "id": post.id,
            "is_original_content": str(post.is_original_content),
            "is_self": str(post.is_self),
            "stickied": str(post.stickied),
            "spoiler": str(post.spoiler),
            "locked": str(post.locked),
            "subreddit_id": post.subreddit_id,
            "view_count": post.view_count if post.view_count is not None else "",
            "contest_mode": str(post.contest_mode),
            "edited": str(post.edited) if post.edited else "False",
            "distinguished": post.distinguished or "",
            "num_crossposts": post.num_crossposts,
        }
        rows.append(data)

    #creating dataframe (spreadsheet)
    df = pd.DataFrame(rows)

    #rename for convenience
    df.rename(columns={
        "title": "Title",
        "author": "Author",
        "upvote_ratio": "Upvote ratio",
        "score": "Score",
        "num_comments": "Number of comments",
        "selftext": "Full text",
        "flair": "Flair",
        "created_utc": "Post time",
        "nsfw": "NSFW status",
        "permalink": "Permalink",
        "url": "URL"
    }, inplace=True)

    #add dataframe into a dictionary
    all_dfs[sub] = df

#save into one Excel file
with pd.ExcelWriter(OUTPUT_EXCEL, engine="openpyxl") as writer:
    for sub, df in all_dfs.items():
        sheet_name = sub[:31]  # Excel limit
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"done! data saved to {OUTPUT_EXCEL}")
