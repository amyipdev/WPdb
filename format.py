class Formatter:
    def __init__(self, post: dict): self.post = post

    def format(self):
        payload = {
            "date": str(self.post["date"]),
            "guid": str(self.post["guid"]),
            "link": str(self.post["link"]),
            "modified": str(self.post["modified"]),
            "title": str(self.post["title"]),
            "content": str(self.post["content"]),
            "author": int(self.post["author"]),
            "excerpt": str(self.post["author"]),
            "featured_media": int(self.post["featured_media"]),
            "categories": str(self.post["categories"]),
            "tags": str(self.post["tags"])
        }
        return payload
