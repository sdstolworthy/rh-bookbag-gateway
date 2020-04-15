from bookbag.models.resource import Resource


def serialize(o):
    print(o.get('metadata'))
    resource = Resource(
        id=o['state']['metadata']['uid'],
        current_state=o['state']['spec']['vars'].get('current_state'),
        provision_data=o['state']['spec']['vars'].get('provision_data'))
    return resource
