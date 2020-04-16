import requests
import os
from bookbag.serializers.resource.backendv1 import serialize


class BackendV1ResourceService(object):
    def __init__(self):
        self.service_token = os.environ.get('OC_SERVICE_TOKEN')
        self.base_url = os.environ.get('OC_API_BASE_URL')

    def get_resources(self):
        response = requests.get(
            self.base_url + '/apis/anarchy.gpte.redhat.com/v1/anarchysubjects',
            verify=False,
            headers={
                'Authorization': 'Bearer {}'.format(self.service_token)
            }).json()
        return [
            serialize(resource_claim) for resource_claim in response['items']
        ]
