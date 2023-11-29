import requests

def get_top_posts(limit=50):
    """Fetches the top posts from Hacker News."""
    top_posts_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(top_posts_url)
    if response.status_code == 200:
        top_post_ids = response.json()[:limit]
        return [get_post_details(post_id) for post_id in top_post_ids]
    else:
        print("Failed to retrieve top posts")
        return []

def get_post_details(post_id):
    """Fetches details of a specific post and returns the post URL and comments URL."""
    post_url = f"https://hacker-news.firebaseio.com/v0/item/{post_id}.json"
    response = requests.get(post_url)
    if response.status_code == 200:
        post_data = response.json()
        post_link = post_data.get('url', 'No URL available')
        comments_link = f"https://news.ycombinator.com/item?id={post_id}"
        return post_link, comments_link
    else:
        print(f"Failed to retrieve details for post ID {post_id}")
        return None, None

if __name__ == "__main__":
    top_posts = get_top_posts()
    for idx, (post_url, comments_url) in enumerate(top_posts, 1):
        print(f"{idx}. Post URL: {post_url}")
        print(f"   Comments URL: {comments_url}\n")
