import feedparser

github_repo_links = [
    "https://github.com/monero-project/monero",
    "https://github.com/monero-project/monero-gui",
    "https://github.com/4rkal/MoneroOS",
    "https://github.com/SChernykh/p2pool",
]

# check for new updates in github repos
def main():
    for repo_link in github_repo_links:
        rss_url = repo_link + "/releases.atom"
        rss_feed = feedparser.parse(rss_url)

        print(rss_feed)
        if rss_feed.entries:
            latest_update = rss_feed.entries[0]
            print(f"Latest update for {repo_link}:")
            print(f"Title: {latest_update.get('title', 'N/A')}")
            print(f"Link: {latest_update.get('link', 'N/A')}")

if __name__ == "__main__":
    main()
