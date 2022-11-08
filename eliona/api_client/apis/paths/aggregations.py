from eliona.api_client.paths.aggregations.get import ApiForget
from eliona.api_client.paths.aggregations.put import ApiForput
from eliona.api_client.paths.aggregations.post import ApiForpost


class Aggregations(
    ApiForget,
    ApiForput,
    ApiForpost,
):
    pass
