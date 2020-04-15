from flask import current_app, Blueprint, g
from bookbag.services.resource_claims import faked_resource_service, backendv1_resource_claim_service

blueprint = Blueprint('resource_claims', __name__)


def get_resource_claim_service():
    return backendv1_resource_claim_service.BackendV1ResourceClaimsService(
        current_app.config.get('OC_SERVICE_TOKEN'))


@blueprint.route('/api/resource_claims', methods=(['GET']))
def get_resource_claims():
    resource_service = get_resource_claim_service()

    # TODO: reach out to OC to get req info
    return {'results': resource_service.get_resource_claims()}
