from flask import current_app, Blueprint, g
from bookbag.services.resource_claims.faked_resource_service import FakedResourceClaimsService

blueprint = Blueprint('resource_claims', __name__)

_resourceClaimService = FakedResourceClaimsService()


@blueprint.route('/api/resource_claims', methods=(['GET']))
def get_resource_claims():
    print(_resourceClaimService)
    # TODO: reach out to OC to get req info
    return {'results': _resourceClaimService.get_resource_claims()}
