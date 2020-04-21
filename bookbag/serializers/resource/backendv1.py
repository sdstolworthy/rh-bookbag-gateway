from bookbag.models.resource import Resource


def serialize(o):

    return Resource(
        id=o['metadata']['uid'],
        governor=o['spec']['governor'],
        provision_messages=o['spec']['vars'].get('provision_messages'),
        current_state=o['spec']['vars'].get('current_state'),
        name=o['metadata']['name'],
        provision_data=o['spec']['vars'].get('provision_data'))
