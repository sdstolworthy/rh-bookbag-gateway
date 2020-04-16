from flask import current_app, Blueprint, Response
import json
from bookbag.services.resources import backendv1_resource_service
blueprint = Blueprint('resources', __name__)


def get_resource_service():
    return backendv1_resource_service.BackendV1ResourceService()


@blueprint.route('/api/resources', methods=(['GET']))
def get_resources():
    resource_service = get_resource_service()

    # TODO: reach out to OC to get req info

    return Response(json.dumps(
        {
            'results': [
                resource_claim
                for resource_claim in resource_service.get_resources()
            ]
        },
        default=lambda o: o.__dict__),
                    mimetype='application/json')
