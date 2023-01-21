from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "postgresql+psycopg2://postgres:12345@localhost:5432/batch1db"
db = create_engine(db_string)

base = declarative_base()


class FilmsORM(base):
    __tablename__ = 'films_orm'
    title = Column(String, primary_key=True)
    director = Column(String)
    year = Column(String)


Session = sessionmaker(db)
sess = Session()

base.metadata.create_all(db)

# insert data to the table
film_one = FilmsORM(
    title="aaaaa",
    director="asasadadf",
    year="2016"
)
sess.add(film_one)
sess.commit()


# create another table "Theatre"
# tablename - Theatre
# thearte_name,established,address
# class TheatreORM(base):
#     __tablename__ = 'theatre_orm'
#     theatre_name = Column(String, primary_key=True)
#     established = Column(String)
#     address = Column(String)

# Session = sessionmaker(db)
# sess = Session()

# base.metadata.create_all(db)

# insert data to the table
# theatre_one = TheatreORM(
#     theatre_name="Theatre1",
#     established="2020",
#     address="WB"
# )
# sess.add(theatre_one)
# sess.commit()

#read from table
films = sess.query(FilmsORM)

for film in films:
    print(film.title,film.director,film.year)


#update
film_one.title = "ASDFG"
sess.commit()

#delete
sess.delete(film_one)
sess.commit()