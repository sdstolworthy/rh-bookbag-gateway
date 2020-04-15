import json


class Resource(object):
    def __init__(self,
                 id=None,
                 current_state=None,
                 provision_data={}):
        self.id = id
        self.current_state = current_state
        self.provision_data = provision_data

    id = ''

    current_state = ''

    provision_data = {}
