from flask import current_app, Blueprint, Response
import json
from bookbag.services.resource_claims import rest_resource_claim_service


blueprint = Blueprint('resource_claims', __name__)


def get_resource_claim_service():
    return rest_resource_claim_service.RestResourceClaimsService(
        current_app.config.get('OC_SERVICE_TOKEN'))


@blueprint.route('/api/resource_claims', methods=(['GET']))
def get_resource_claims():
    resource_service = get_resource_claim_service()

    # TODO: reach out to OC to get req info

    return Response(json.dumps(
        {
            'results': [
                resource_claim
                for resource_claim in resource_service.get_resource_claims()
            ]
        },
        default=lambda o: o.__dict__),
                    mimetype='application/json')
