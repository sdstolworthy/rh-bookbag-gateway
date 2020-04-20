import requests
import os
from bookbag.serializers.resource_claims.backendv1 import serialize


class RestResourceClaimsService(object):
    def __init__(self, token):
        self.service_token = os.environ.get('OC_SERVICE_TOKEN')
        self.base_url = os.environ.get('OC_API_BASE_URL')

    def get_resource_claims(self):
        response = requests.get(
            self.base_url + '/apis/poolboy.gpte.redhat.com/v1/resourceclaims',
            verify=False,
            headers={
                'Authorization': 'Bearer {}'.format(self.service_token)
            }).json()
        return [
            serialize(resource_claim) for resource_claim in response['items']
        ]
