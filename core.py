from ast import Invert
from sqlalchemy.orm import aliased
from sqlalchemy import insert
from models import worker_t

from database import sync_engine
from models import metadata_obj

def create_table():
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)

def insert_data():
    with sync_engine.connect() as conn:
        # stmt = """INSERT INTO workers VALUES (NULL, 'daler', 'kurbonbekov23mail.com')"""
        
        stmt = insert(worker_t).values(username='ashot', email="ashot35@gmail.com")
        stmt = insert(worker_t).values(username='daler', email="dalerchic34@gmail.com")
        conn.execute(stmt)
        conn.commit()