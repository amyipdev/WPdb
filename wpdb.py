from errors.dbtypeerror import DBTypeError
from errors.locationerror import LocationError
from os import path
from wp import WPHandler
from format import Formatter
from sql import SQLHandler


class WPdb:
    # currently the only valid db type (dbt) is "sqlite3"
    # we're working on adding postgresql and some others
    # mysql is probably the top priority at the moment
    # that'll probably take an x.0.0 update to factor, though
    # and isn't a priority at the moment, but it will be done
    # considering that it would basically take a complete rewrite
    # of all the programming logic, .db files are transferrable,
    # and it would completely break any backwards API compatibilty
    # see the to do in sql.py
    def __init__(self, site: str, dbt: str, dbl: str):
        self.site = site
        self.dbt = dbt
        self.dbl = dbl
        if self.dbt != "sqlite3": raise DBTypeError("this database type isn't supported yet")
        if not path.isfile(dbl): raise LocationError("this isn't a valid db file location")

    def run(self):
        wph = WPHandler(site=self.site)
        posts = wph.get_posts()
        sqlh = SQLHandler(db=self.dbl)
        for post in posts:
            fmt = Formatter(post)
            payload = fmt.format()
            sqlh.push(payload=payload)
        sqlh.end()


def main():
    instance = WPdb(site=input("website to pull: "),
                    dbt=input("database type (sqlite3): "),
                    dbl=input("database file (example: x.db): "))
    instance.run()


if __name__ == "__main__": main()
