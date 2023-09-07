import feedparser
from datetime import datetime, timedelta
import pytz

github_repo_links = [
    "https://github.com/monero-project/monero",
    "https://github.com/monero-project/monero-gui",
    "https://github.com/4rkal/MoneroOS",
    "https://github.com/SChernykh/p2pool",
    "https://github.com/hinto-janai/gupax",
    "https://github.com/hinto-janai/monero-vanity",
]

now = datetime.utcnow()
now = now.date()
one_week_ago = now - timedelta(days=7)
print(one_week_ago)
print(now)

# check for new updates in github repos
def main():
    for repo_link in github_repo_links:
        rss_url = repo_link + "/releases.atom"
        rss_feed = feedparser.parse(rss_url)

        # print(rss_feed)
        if rss_feed.entries:
            latest_update = rss_feed.entries[0]
            release_date = latest_update.get('updated')
            release_date = datetime.fromisoformat(release_date).replace(tzinfo=pytz.UTC)
            release_date = release_date.date()
            # print(release_date)
            if one_week_ago <= release_date <= now:
                # print(latest_update)
                print(f"Latest update for {repo_link}:")
                print(f"Title: {latest_update.get('title', 'N/A')}")
                print(f"Link: {latest_update.get('link', 'N/A')}")
                print(f"Latest Update: {release_date} ")
                print()

if __name__ == "__main__":
    main()
