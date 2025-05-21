import praw
import pandas as pd

reddit = praw.Reddit("bot1", user_agent="bot1 user agent")

subreddit_name = "deeplearning"
subreddit = reddit.subreddit(subreddit_name)
sort_by_method = "top"
submission_rows = []
comment_rows = []
submission_row_keys = {"id", "title", "upvote_ratio", "score", "selftext", "poll_data", "over_18", "num_comments", "locked", "is_self", "author", "author_flair_text", "url", "link_flair_text"}
comment_row_keys = {"id", "parent_id", "score", "body", "created_utc", "is_submitter", "author"}
for submission in subreddit.__getattr__(sort_by_method)(limit=50, time_filter="all"):
    submission_row = {key:getattr(submission, key, None) for key in submission_row_keys}
    for comment in submission.comments:        
        comment_row = {key:getattr(comment, key, None) for key in comment_row_keys}
        comment_rows.append(comment_row)
    submission_rows.append(submission_row)

df_submissions = pd.DataFrame(submission_rows)
df_comments = pd.DataFrame(comment_rows)

df_submissions.to_csv(f"{subreddit_name}_submissions_{sort_by_method}.csv", index=False)
df_comments.to_csv(f"{subreddit_name}_comments_{sort_by_method}.csv", index=False)

