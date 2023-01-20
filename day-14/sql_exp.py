from sqlalchemy import create_engine
from sqlalchemy import Table,Column,String,MetaData

db_string = "postgresql+psycopg2://postgres:12345@localhost:5432/batch1db"
db = create_engine(db_string)

meta = MetaData(db)

film_table = Table(
    'films_exp',
    meta,
    Column('title',String),
    Column('director',String),
    Column('year',String)
)

with db.connect() as conn:
    # create table
    film_table.create()
    insert_statement = film_table.insert().values(
        title ="Doctor Strange 50",
        director = "Rohit Shetty",
        year = "2050"
    )
    conn.execute(insert_statement)