from flask import Blueprint
from .models import FakedResourceClaimFactory

blueprint = Blueprint('resource_claims', __name__)


@blueprint.route('/api/resource_claims', methods=(['GET']))
def get_resource_claims():
    # TODO: reach out to OC to get req info
    return {'results': [FakedResourceClaimFactory().dump() for _ in range(10)]}
