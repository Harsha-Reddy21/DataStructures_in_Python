from collections import Counter, defaultdict

users = {
    "alice": {"followers": 150, "following": 75},
    "bob": {"followers": 89, "following": 120}
}

posts = [
    {"id": 1, "user": "alice", "content": "Love Python Programming", "likes": 15, "tags": ["python", "coding"]},
    {"id": 2, "user": "bob", "content": "Great weather today", "likes": 8, "tags": ["life", "weather"]},
    {"id": 3, "user": "alice", "content": "Data structures are fun", "likes": 22, "tags": ["python", "learning"]},
]


all_tags = []
for post in posts:
    all_tags.extend(post["tags"])

tag_counter = Counter(all_tags)

print("Most Popular Tags:")
for tag, count in tag_counter.most_common():
    print(f"{tag}: {count}")


likes_per_user = defaultdict(int)
for post in posts:
    likes_per_user[post["user"]] += post["likes"]

print("\nUser Engagement (Total Likes):")
for username in users:
    print(f"{username}: {likes_per_user[username]} likes")

top_posts = sorted(posts, key=lambda x: x["likes"], reverse=True)

print("\nTop Posts by Likes:")
for post in top_posts:
    print(f"Post ID {post['id']} by {post['user']}: {post['likes']} likes")

user_summary = defaultdict(lambda: {"posts": 0, "likes": 0, "followers": 0, "following": 0})

for post in posts:
    user = post["user"]
    user_summary[user]["posts"] += 1
    user_summary[user]["likes"] += post["likes"]

for user in users:
    user_summary[user]["followers"] = users[user]["followers"]
    user_summary[user]["following"] = users[user]["following"]

print("\nUser Activity Summary:")
for user, summary in user_summary.items():
    print(f"{user} Posts: {summary['posts']}, Likes: {summary['likes']}, "
          f"Followers: {summary['followers']}, Following: {summary['following']}")
