import requests
import os
import json


class RestCustomObjectApi(object):
    def __init__(self):
        self.service_token = os.environ.get('OC_SERVICE_TOKEN')
        self.base_url = os.environ.get('OC_API_BASE_URL')

    def get_namespaced_custom_object(self, api, version, namespace,
                                     object_type, identifier):
        request_url = self.base_url + '/apis/{api}/{version}/namespaces/{namespace}/{object_type}/{identifier}'.format_map(
            {
                'api': api,
                'namespace': namespace,
                'version': version,
                'object_type': object_type,
                'identifier': identifier
            })
        response = requests.get(request_url,
                                verify=False,
                                headers={
                                    'Authorization':
                                    'Bearer {}'.format(self.service_token)
                                }).json()
        return response

    def create_namespaced_custom_object(self, api, version, namespace,
                                        object_type, spec):
        url = self.base_url + '/apis/{api}/{version}/namespaces/{namespace}/{object_type}'.format_map(
            {
                'api': api,
                'namespace': namespace,
                'version': version,
                'object_type': object_type,
            })
        response = requests.post(url,
                                 json=spec,
                                 verify=False,
                                 headers={
                                     'Authorization':
                                     'Bearer {}'.format(self.service_token),
                                     'Content-Type':
                                     'application/json'
                                 }).json()
        return response