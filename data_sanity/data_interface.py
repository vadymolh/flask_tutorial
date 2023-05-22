import requests
import json

CMS_TOKEN = "skJ1rViXjd1ZFxMijG56hJFFdiMBm0zn5RPpm0aCRalelJ8bvBTjOngZY9jfv0oRo65ARntRZBwX298RM69G3RkMyJPHoCkXvfoAQ87uITCzS4l8ppV95reVVYy9CkdPzJIYuuP8IoV1bHsUxhTI6aRfkt27b0WdRFnOf5rgHHbFQDyWuqW6"
headers = {"Authorization": "Bearer " + CMS_TOKEN}
endpoint= "v2021-06-07/data/query/production?query="

URL = "https://vikcf4el.api.sanity.io/"


def get_all_posts():
    query = "*[_type == 'post']"
    data = requests.get(f"{URL}{endpoint}{query}", headers= headers)

    data = data.json()
    posts = []
    print(data)
    for post in data['result']:
        title = post['title']
        content = post['content']
        posts.append({'title':title, 'text':content})
    return posts
