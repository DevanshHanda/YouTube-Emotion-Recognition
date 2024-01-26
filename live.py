import requests
import json

def stream_user_posts(user_id):
    # Set up the stream
    url = "https://api.mastodon.cloud/v1/streaming/timeline?user={}&format=json".format(user_id)
    headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
    stream = requests.get(url, headers=headers, stream=True)

    # Process the stream
    for line in stream.iter_lines():
        if line:
            try:
                data = json.loads(line.decode("utf-8"))
                if "content" in data:
                    print(data["content"])
            except json.JSONDecodeError:
                pass

# Get the user ID
user_id = input("Enter the user ID: ")

# Start streaming the user's posts
stream_user_posts(user_id)

