import faker



def fake_filling_form_who_is_the_scooter():
    fake = faker.Faker('ru_Ru')
    name = fake.first_name()[0:10]
    second_name = fake.last_name()[0:10]
    address = fake.street_address()[0:20].replace('/', '')
    telephone = fake.msisdn()[0:12]
    return name, second_name, address, telephone

def fake_comment():
    fake = faker.Faker('ru_Ru')
    comment = f'Для {fake.name()}'
    return comment