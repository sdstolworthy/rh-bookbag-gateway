import requests
import os
import json

class RestCustomObjectApi(object):
    def __init__(self):
        self.service_token = os.environ.get('OC_SERVICE_TOKEN')
        self.base_url = os.environ.get('OC_API_BASE_URL')

    def get_namespaced_custom_object(self, api, version, namespace,
                                     object_type, identifier):
        response = requests.get(
            self.base_url +
            '/apis/{api}/{version}/{object_type}/{identifier}'.format_map(
                {
                    'api': api,
                    'version': version,
                    'object_type': object_type,
                    'identifier': identifier
                }),
            verify=False,
            headers={
                'Authorization': 'Bearer {}'.format(self.service_token)
            }).json()
        return response

    def create_namespaced_custom_object(self, api, version, namespace,
                                        object_type, spec):
        response = requests.get(
            self.base_url + '/apis/{api}/{version}/{object_type}'.format_map(
                {
                    'api': api,
                    'version': version,
                    'object_type': object_type,
                }),
            json=json.dumps(spec),
            verify=False,
            headers={
                'Authorization': 'Bearer {}'.format(self.service_token),
                'Content-Type': 'application/json'
            }).json()
        return response