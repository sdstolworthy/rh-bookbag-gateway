import requests
import os

class BackendV1ResourceClaimsService(object):
    def __init__(self, token):
        self.service_token = os.environ.get('OC_SERVICE_TOKEN')
        self.base_url = os.environ.get('OC_API_BASE_URL')

    def get_resource_claims(self):
        return requests.get(
            self.base_url +
            '/apis/apiextensions.k8s.io/v1beta1/customresourcedefinitions?fieldSelector=metadata.name=resourceclaims.poolboy.gpte.redhat.com',
            verify=False,
            headers={
                'Authorization': 'Bearer {}'.format(self.service_token)
            }).json()
