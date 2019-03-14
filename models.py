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


class BaseModelMixin(object):
    '''
    This class is used to extend the SQLAlchemy declarative_base, allowing us to add standard
    boilerplate fields to all models using it as a mixin.
    '''
    # this tells continuum to version this model's records
    __versioned__ = {}
    # these are fields that we want to be common to every model, as not to be repetitive
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.TIMESTAMP(timezone=True), server_default=func.now())
    updated_date = sa.Column(sa.TIMESTAMP(timezone=True), onupdate=func.now())

class Customer(BaseModelMixin, Base):
    __tablename__ = 'customer'

    first_name = sa.Column(sa.Unicode(255))
    last_name = sa.Column(sa.Unicode(255))

    addresses = relationship("Address", backref="customer")

    created_date = sa.Column(sa.TIMESTAMP(timezone=True), server_default=func.now())
    updated_date = sa.Column(sa.TIMESTAMP(timezone=True), onupdate=func.now())


class Address(BaseModelMixin, Base):
    __tablename__ = 'address'

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