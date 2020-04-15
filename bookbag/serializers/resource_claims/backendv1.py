from bookbag.models.resource_claim import ResourceClaim
from bookbag.serializers.resource.backendv1 import serialize as serialize_resource


def serialize(o):
    resource_claim = ResourceClaim(id=o['metadata']['uid'],
                                   current_state='started',
                                   name=o['metadata']['name'],
                                   resources=[
                                       serialize_resource(resource)
                                       for resource in o['status']['resources']
                                   ])
    return resource_claim