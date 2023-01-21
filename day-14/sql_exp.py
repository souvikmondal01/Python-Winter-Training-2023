from sqlalchemy import create_engine
from sqlalchemy import Table,Column,String,MetaData

db_string = "postgresql+psycopg2://postgres:12345@localhost:5432/batch1db"
db = create_engine(db_string)

meta = MetaData(db)

film_table = Table(
    'films_exp_d26',
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

    # read from table
    print("Reading from table")
    select_statement = film_table.select()
    select_result = conn.execute(select_statement)
    for r in select_result:
        print(r)

    # update table
    print("Updating")
    print(film_table.c)
    update_statement = film_table.update().where(
        film_table.c.year == '2016'
    ).values(title="Amazing Spiderman")
    conn.execute(update_statement)

    # delete
    print("Delete operation")
    delete_statement = film_table.delete().where(
        film_table.c.year == '2016'
    )
    conn.execute(delete_statement)


