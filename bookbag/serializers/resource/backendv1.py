from bookbag.models.resource import Resource


def serialize(o):
    resource = Resource(
        id=o['metadata']['uid'],
        current_state=o['spec']['vars'].get('current_state'),
        provision_data=o['spec']['vars'].get('provision_data'))
    return resource
