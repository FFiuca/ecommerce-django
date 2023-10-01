from faker import Faker
import faker_commerce

class FakerHelper:
    def __init__(self)-> None:
        self.fake = Faker(['id_ID'])

        self.fake.add_provider(faker_commerce.Provider)
