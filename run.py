from models import Customer, Address, session

if __name__ == '__main__':
    # create a customer and address record
    customer = Customer(first_name='Jane', last_name='Doe')
    customer.addresses.append(Address(type='home', street='123 Fake St', city='B-lo', postal_code='14203'))
    customer.addresses.append(Address(type='work', street='123 Sand Hill Road', city='SF', postal_code='94103'))

    # write the objects to the DB
    session.add(customer)
    session.commit()

    # modify our customer record
    customer.last_name = 'Doe-Simpson'

    # delete old address
    session.query(Address).filter_by(customer=customer, type="home").delete()

    # add new address
    customer.addresses.append(Address(type='home', street='145 Delaware Ave', city='B-Lo', postal_code='14202'))

    session.add(customer)
    session.commit()

    for version in customer.versions:
        print(version.last_name)

