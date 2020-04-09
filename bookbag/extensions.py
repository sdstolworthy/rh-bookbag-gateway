from flask_cors import CORS
from faker import Faker
from faker.providers import lorem

cors = CORS()
faker = Faker(['en_US'],
              providers=[
                  'faker.providers.misc', 'faker.providers.lorem',
                  'faker.providers.internet', 'faker.providers.person',
                  'faker.providers.company'
              ])


class Factory(object):
    def __init__(self, schema, defaults={}):
        self.schema = schema
        self.defaults = {}
        self.defaults.update(defaults)

    def complete(self, data={}):
        complete_data = {}
        complete_data.update(self.defaults)
        complete_data.update(data)
        return complete_data

    def dump(self, data={}, *args, **kwargs):
        return self.schema.dump(self.complete(data), *args, **kwargs)

    def dumps(self, data={}, *args, **kwargs):
        return self.schema.dumps(self.complete(data), *args, **kwargs)