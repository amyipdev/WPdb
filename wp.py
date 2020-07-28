import requests


# noinspection PyMethodMayBeStatic
class WPHandler:
    def __init__(self, site: str): self.site = f"{site}/wp-json/wp/v2/"

    def get_posts(self):
        posts = []
        page_number = 1
        flag = True
        while flag:
            params = {
                "per_page": "100",
                "page": page_number
            }
            r = requests.get(f"{self.site}posts", params=params)
            posts_list = r.json()
            for post in posts_list: posts.append(post)
            if len(posts_list) < 100: flag = False
            page_number += 1
        return posts
