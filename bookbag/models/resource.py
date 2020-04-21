import json


class Resource(object):
    def __init__(self,
                 id=None,
                 current_state=None,
                 name="",
                 provision_data={},
                 provision_messages=[],
                 governor=None):
        self.provision_messages = provision_messages
        self.name = name
        self.id = id
        self.governor = governor
        self.current_state = current_state
        self.provision_data = provision_data

    id = ''

    provision_messages = []

    name = ""

    governor = ''

    current_state = ''

    provision_data = {}
