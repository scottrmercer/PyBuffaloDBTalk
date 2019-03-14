import logging

import sqlalchemy as sa
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# configure info level logging to see SQL output in stdout
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# initialize the DB connection and model base class
engine = create_engine('postgres://postgres:postgres@postgres')
session = sessionmaker(bind=engine)()
Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.TIMESTAMP(timezone=True), server_default=func.now())
    updated_date = sa.Column(sa.TIMESTAMP(timezone=True), onupdate=func.now())

    first_name = sa.Column(sa.Unicode(255))
    last_name = sa.Column(sa.Unicode(255))

    addresses = relationship("Address", backref="customer")

    created_date = sa.Column(sa.TIMESTAMP(timezone=True), server_default=func.now())
    updated_date = sa.Column(sa.TIMESTAMP(timezone=True), onupdate=func.now())


class Address(Base):
    __tablename__ = 'address'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.TIMESTAMP(timezone=True), server_default=func.now())
    updated_date = sa.Column(sa.TIMESTAMP(timezone=True), onupdate=func.now())

    customer_id = sa.Column(sa.Integer, sa.ForeignKey('customer.id'), nullable=False)

    type = sa.Column(sa.Unicode(20))
    street = sa.Column(sa.Unicode(255))
    city = sa.Column(sa.Unicode(255))
    postal_code = sa.Column(sa.Unicode(8))

    created_date = sa.Column(sa.TIMESTAMP(timezone=True), server_default=func.now())
    updated_date = sa.Column(sa.TIMESTAMP(timezone=True), onupdate=func.now())


# Generates a fresh schema from the models (only runs once)
Base.metadata.create_all(engine)

print ('Current Tables:')
for table in engine.table_names():
    print(f'{table}')