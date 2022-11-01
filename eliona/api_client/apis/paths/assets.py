from eliona.api_client.paths.assets.get import ApiForget
from eliona.api_client.paths.assets.put import ApiForput
from eliona.api_client.paths.assets.post import ApiForpost


class Assets(
    ApiForget,
    ApiForput,
    ApiForpost,
):
    pass
