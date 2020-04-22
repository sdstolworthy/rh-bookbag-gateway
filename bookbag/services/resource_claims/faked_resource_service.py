from bookbag.schemas.resource_claim import FakedResourceClaimFactory

class FakedResourceClaimsService(object):
    def __init__(self):
        pass
    def get_resource_claims(self):
        return [FakedResourceClaimFactory().dump() for _ in range(10)]
