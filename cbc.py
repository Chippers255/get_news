import feedparser

def read_cbc_top_stories_rss_feed():
    # URL of the CBC News top stories RSS feed
    rss_feed_url = "https://www.cbc.ca/webfeed/rss/rss-topstories"

    # Parse the RSS feed
    feed = feedparser.parse(rss_feed_url)

    if feed.get('entries'):
        # Print the top story titles and links
        for entry in feed.entries:
            title = entry.get('title', 'No Title')
            link = entry.get('link', 'No Link')
            print(f"Title: {title}")
            print(f"Link: {link}\n")
    else:
        print("No top stories found in the RSS feed.")

if __name__ == "__main__":
    read_cbc_top_stories_rss_feed()
