from random import Random
from faker import Faker


def get_customer_credentials(customer_state: str):
    """
    :param customer_state: 'new_customer' or 'exist_customer'
    :return:
    """
    random = Random()
    random_int = random.randint(1, 9999999)
    fake = Faker('en_US')
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f'max093213_auto_test_{first_name}_{last_name}_{random_int}@gmail.com'

    get_customer_credentials_data = {
        'new_customer': {
            'first_name': first_name,
            'last_name': last_name,
            'customer_email': email
        },
        'exist_customer': {
            'first_name': 'Max',
            'last_name': 'Ishchenko',
            'customer_email': 'example@gmail.com'
        }
    }
    if customer_state in get_customer_credentials_data:
        return get_customer_credentials_data[customer_state]
    raise Exception(f'{customer_state} - not found')


def get_customer_address(customer_locale: str):
    """
    :param customer_locale: 'DE', 'CH'
    :return:
    """
    address_data = {
        'DE': {
            'zip': '04084',
            'city': 'Kiev',
            'house_number': '28',
            'street': 'Dancenka',
            'dob_day': '20',
            'dob_month': '06',
            'dob_year': '1988',
            'phone_number': '4565656'
        },
        'CH': {
            'zip': '04084',
            'city': 'Kiev',
            'house_number': '28',
            'street': 'Dancenka',
            'dob_day': '20',
            'dob_month': '06',
            'dob_year': '1988',
            'phone_number': '4565656'
        }
    }
    if customer_locale in address_data:
        return address_data[customer_locale]
    raise Exception(f'{customer_locale} - not found')
