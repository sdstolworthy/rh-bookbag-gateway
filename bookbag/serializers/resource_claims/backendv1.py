from bookbag.models.resource_claim import ResourceClaim
from bookbag.serializers.resource.backendv1 import serialize as serialize_resource


def serialize(o):
    resource_claim = ResourceClaim(
        id=o['metadata']['uid'],
        current_state='started',
        name=o['metadata']['name'],
        resources=[
            serialize_resource(resource.get('state'))
            for resource in o['status']['resources']
        ],
        namespace=o['metadata']['namespace'],
        resource_handle_name=o['status'].get('resourceHandle').get('name'),
    )
    return resource_claim