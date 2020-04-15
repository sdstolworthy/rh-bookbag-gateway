from bookbag.extensions import Factory, faker
import json


class ResourceClaim(object):
    def __init__(self, id=None, current_state=None, name=None, resources=[]):
        self.id = id
        self.name = name
        self.resources = resources

    id = ''

    current_state = None

    name = None

    resources = []


class FakedResourceClaimFactory(Factory):
    def __init__(self):
        super().__init__(ResourceClaim(),
                         defaults={
                             'id': faker.random_digit(),
                             'name': ''.join(faker.words(nb=3)),
                             'resources': [],
                         })
