class Community:
    def __init__(self, name, description, member_count, posts):
        self.name = name
        self.description = description
        self.members = member_count
        self.posts = posts

    def add_post(self, _P):
        self.posts.append(_P)

class Post:
    def __init__(self, community, title, body, upvotes, downvotes):
        self.upvotes = upvotes
        self.title = title
        self.body = body
        self.downvotes = downvotes
        self.community = community