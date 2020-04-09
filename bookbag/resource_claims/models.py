from marshmallow import (Schema, fields, validate)
from bookbag.extensions import Factory, faker


class ResourceClaim(Schema):
    id = fields.Int()
    current_state = fields.String(
        validate=validate.ContainsOnly(['started', 'stopped']))
    name = fields.String()
    provision_data = fields.Dict(keys=fields.String)


class FakedResourceClaimFactory(Factory):
    def __init__(self):
        super().__init__(ResourceClaim(),
                         defaults={
                             'id': 1,
                             'name': 'asdfasdf',
                             'provision_data': {
                                 'hello': 'hi'
                             }
                         })
