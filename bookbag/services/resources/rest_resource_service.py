import requests
import os
from bookbag.serializers.resource.backendv1 import serialize
import json


class RestResourceService(object):
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

    def modify_resource_state(self, resource_name, operation):
        patch_action = ''
        if operation == 'start':
            patch_action = 'started'
        elif operation == 'stop':
            patch_action == 'stopped'
        else:
            raise TypeError('operation must be one of \'start\' or \'stop\'')
        request_url = self.base_url + '/apis/anarchy.gpte.redhat.com/v1/namespaces/anarchy-operator/anarchysubjects/{}'.format(
            resource_name)
        print(request_url)
        response = requests.patch(request_url.format(resource_name),
                                  verify=False,
                                  headers={
                                      'Authorization':
                                      'Bearer {}'.format(self.service_token),
                                      'Content-Type':
                                      'application/json-patch+json'
                                  },
                                  json=[{
                                      'op': 'replace',
                                      'path': '/spec/vars/desired_state',
                                      'value': 'stopped'
                                  }]).json()
        return serialize(response)
