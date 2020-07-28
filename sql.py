import sqlite3
from sqlite3 import Error as SQLiteGeneralError
from sqlite3 import OperationalError


# todo: add mysql, postgresql, oracle, sql server support
# todo: have a db config system


# noinspection SqlNoDataSourceInspection
class SQLHandler:
    def __init__(self, db: str):
        self.conn = None
        try: self.conn = sqlite3.connect(db)
        except SQLiteGeneralError as sqlge: print(sqlge)
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * from posts;")
        except OperationalError:
            cur = self.conn.cursor()
            cur.execute("CREATE TABLE posts ( "
                        "date string,"
                        "guid string,"
                        "link string,"
                        "modified string,"
                        "title string,"
                        "content string,"
                        "author int,"
                        "excerpt string,"
                        "featured_media int,"
                        "categories string,"
                        "tags string"
                        ");")

    def push(self, payload: dict):
        cur = self.conn.cursor()
        data = (payload["date"],
                payload["guid"],
                payload["link"],
                payload["modified"],
                payload["title"],
                payload["content"],
                payload["author"],
                payload["excerpt"],
                payload["featured_media"],
                payload["categories"],
                payload["tags"],)
        cur.execute("INSERT INTO posts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)

    def end(self):
        self.conn.commit()
        self.conn.close()
