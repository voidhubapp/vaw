import requests
from .abc import Community, Post

class VoidHub:
    def __init__(self, v_url = "http://127.0.0.1:5000"):
        self.to = v_url

    def community(self, name):
        contents = requests.get(f"{self.to}/v/{name}/json").json()
        c = Community(contents["meta"]["name"], contents["meta"]["display_name"], int(contents["meta"]["members"]), [])
        posts = contents["posts"]
        for P in posts.keys():
            c.add_post(Post(c, posts[P]["title"], posts[P]["body"], posts[P]["upvotes"], posts[P]["downvotes"]))

        return c