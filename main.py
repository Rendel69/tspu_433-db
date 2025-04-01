import sqlite3

from ddl import create_tale_authors
from dml import add_authors
connection = sqlite3.connect('database.sqlite')
create_tale_authors(connection)

add_authors(connection)


print("Hello, World!")

print("Hello,World!")
connection.close()
