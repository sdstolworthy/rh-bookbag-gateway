from flask import current_app, Blueprint, Response, request
import json
from bookbag.services.resources import rest_resource_service
blueprint = Blueprint('resources', __name__)


def get_resource_service():
    return rest_resource_service.RestResourceService()


@blueprint.route('/api/resources', methods=(['GET']))
def get_resources():
    resource_service = get_resource_service()

    return Response(json.dumps(
        {
            'results':
            [resource for resource in resource_service.get_resources()]
        },
        default=lambda o: o.__dict__),
                    mimetype='application/json')


@blueprint.route('/api/resources/<name>', methods=(['PATCH']))
def modify_desired_resource_state(name):
    operation = request.get_json()['operation']
    resource_service = get_resource_service()
    modified_resource = resource_service.modify_resource_state(name, operation)
    return Response(json.dumps(modified_resource,
                               default=lambda o: o.__dict__),
                    mimetype='application/json')
