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


@blueprint.route('/api/resources/dispatch/<namespace>/<name>/<action>',
                 methods=(['GET']))
def dispatch_resource_action(namespace, name, action):
    try:
        resource_service = get_resource_service()
        resource_service.dispatch_custom_action(action, namespace, name)
        return Response(status=200)
    except:
        return Response(status=500)


@blueprint.route('/api/resources/modify/<name>', methods=(['PATCH']))
def modify_desired_resource_state(name):
    operation = request.get_json()['operation']
    resource_service = get_resource_service()
    modified_resource = resource_service.modify_resource_state(name, operation)
    return Response(json.dumps(modified_resource,
                               default=lambda o: o.__dict__),
                    mimetype='application/json')
