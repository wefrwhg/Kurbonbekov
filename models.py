from sqlalchemy import Table, Column, Integer, String, MetaData

metadata_obj = MetaData()

worker_t = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String),
    Column("email", String)
)