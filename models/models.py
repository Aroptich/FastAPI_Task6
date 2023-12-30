from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, DECIMAL


metadata = MetaData()

items = Table(
    'items',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(80), nullable=False),
    Column('description', String(300), nullable=False),
    Column('price', DECIMAL, nullable=False),
)

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(80), nullable=False),
    Column('email', String(80), nullable=False),
    Column('password', String(80), nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.utcnow),

)

orders = Table(
    'oreders',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('item_id', Integer, ForeignKey('items.id')),
)