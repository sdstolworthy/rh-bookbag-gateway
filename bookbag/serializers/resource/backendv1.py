from bookbag.schemas.resource import Resource


def serialize(o):
    return Resource(
        id=o['metadata']['uid'],
        governor=o['spec']['governor'],
        provision_messages=o['spec']['vars'].get('provision_messages'),
        current_state=o['spec']['vars'].get('current_state'),
        name=o['metadata']['name'],
        job_vars=o['spec']['vars'].get('job_vars'),
        tower_jobs=o['status'].get('towerJobs')
        if o.get('status') is not None else [],
        deletion_timestamp=o['metadata'].get('deletionTimestamp'),
        provision_data=o['spec']['vars'].get('provision_data'))
