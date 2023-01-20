from sqlalchemy import create_engine

db_string = "postgresql+psycopg2://postgres:12345@localhost:5432/batch1db"
db = create_engine(db_string)

db.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")
db.execute("INSERT INTO films (title,director,year) VALUES ('Doctor Strange','Scott','2016')")

result = db.execute("SELECT * FROM films")
for r in result:
    print(r)
print(result)

# db.execute("UPDATE films SET title='Some2016Films' WHERE year = '2016")
# db.execute("DELETE FROM films WHERE year = '2016")
