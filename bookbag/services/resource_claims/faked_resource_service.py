from bookbag.schemas.resource_claim import FakedResourceClaimFactory


class FakedResourceClaimsService(object):
    def __init__(self):
        pass

    def get_resource_claims(self):
        return [FakedResourceClaimFactory().dump() for _ in range(10)]

    def delete_resource_claim(self, claim_namespace, claim_name):
        print('Deleting {}'.format(claim_name))
