import json


class Resource(object):
    def __init__(self,
                 id=None,
                 current_state=None,
                 name="",
                 tower_jobs=[],
                 job_vars={},
                 provision_data={},
                 provision_messages=[],
                 deletion_timestamp='',
                 namespace='',
                 governor=None):
        self.provision_messages = provision_messages
        self.name = name
        self.namespace = namespace
        self.deletion_timestamp = deletion_timestamp
        self.id = id
        self.job_vars = job_vars
        self.tower_jobs = tower_jobs
        self.governor = governor
        self.current_state = current_state
        self.provision_data = provision_data

    id = ''

    namespace = ''

    deletion_timestamp = ''

    tower_jobs = []

    job_vars = {}

    provision_messages = []

    name = ""

    governor = ''

    current_state = ''

    provision_data = {}
