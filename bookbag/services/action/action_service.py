from requests import request
from bookbag.services.custom_object_service.rest_custom_object_api import RestCustomObjectApi

class RestActionService(object):
    def __init__(self):
        pass

    def create_custom_action(self, action_name, namespace, subject_name):
        __create_subject_action(action_name, namespace, subject_name)


def __create_subject_action(action_name, namespace, subject_name):
    custom_objects_api = RestCustomObjectApi()

    anarchy_subject = custom_objects_api.get_namespaced_custom_object(
        'anarchy.gpte.redhat.com', 'v1', namespace, 'anarchysubjects',
        subject_name)
    anarchy_governor = custom_objects_api.get_namespaced_custom_object(
        'anarchy.gpte.redhat.com', 'v1', namespace, 'anarchygovernors',
        anarchy_subject['spec']['governor'])

    anarchy_action = custom_objects_api.create_namespaced_custom_object(
        'anarchy.gpte.redhat.com',
        'v1',
        namespace,
        'anarchyactions',
        {
            "apiVersion": "anarchy.gpte.redhat.com/v1",
            "kind": "AnarchyAction",
            "metadata": {
                "generateName":
                "{0}-{1}-".format(subject_name, action_name),
                "labels": {
                    "anarchy.gpte.redhat.com/action":
                    action_name,
                    "anarchy.gpte.redhat.com/governor":
                    anarchy_subject['spec']['governor'],
                    "anarchy.gpte.redhat.com/subject":
                    subject_name
                },
                "namespace":
                namespace,
                "ownerReferences": [{
                    "apiVersion": "anarchy.gpte.redhat.com/v1",
                    "controller": True,
                    "kind": "AnarchySubject",
                    "name": subject_name,
                    "uid": anarchy_subject['metadata']['uid']
                }],
            },
            "spec": {
                "action": action_name,
                #"after": "2020-04-08T18:18:13Z",
                #"callbackToken": "...",
                "governorRef": {
                    "apiVersion": "anarchy.gpte.redhat.com/v1",
                    "kind": "AnarchyGovernor",
                    "name": anarchy_governor['metadata']['name'],
                    "namespace": namespace,
                    "uid": anarchy_governor['metadata']['uid']
                },
                "subjectRef": {
                    "apiVersion": "anarchy.gpte.redhat.com/v1",
                    "kind": "AnarchySubject",
                    "name": subject_name,
                    "namespace": namespace,
                    "uid": anarchy_subject['metadata']['uid']
                }
            }
        })
    return anarchy_action