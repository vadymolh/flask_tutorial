import requests
import json

CMS_TOKEN = "skJ1rViXjd1ZFxMijG56hJFFdiMBm0zn5RPpm0aCRalelJ8bvBTjOngZY9jfv0oRo65ARntRZBwX298RM69G3RkMyJPHoCkXvfoAQ87uITCzS4l8ppV95reVVYy9CkdPzJIYuuP8IoV1bHsUxhTI6aRfkt27b0WdRFnOf5rgHHbFQDyWuqW6"
headers = {"Authorization": "Bearer " + CMS_TOKEN}
endpoint= "v2021-06-07/data/query/production?query="

CDN = "https://cdn.sanity.io/images/vikcf4el/production/"

URL = "https://vikcf4el.api.sanity.io/"

def form_image_url(ref):
    image_ref = ref.replace('image-', '')
    i = len(image_ref)-1
    ext_index = image_ref.find("-",i-5, i)
    image_name = image_ref[:ext_index] + "." + image_ref[ext_index+1:]
    return CDN + image_name
    

def get_all_posts():
    query = "*[_type == 'post']"
    data = requests.get(f"{URL}{endpoint}{query}", headers= headers)

    data = data.json()
    posts = []
    print(data)
    for post in data['result']:
        title = post['title']
        content = post['content']
        if 'asset' in post['post_image']:
            image_ref = post['post_image']['asset']['_ref']
            image_url = form_image_url(image_ref)
        posts.append({'title':title, 'text':content, 'image_url':image_url})
    return posts
