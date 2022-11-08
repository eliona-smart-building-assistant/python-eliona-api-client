from eliona.api_client.paths.asset_types.get import ApiForget
from eliona.api_client.paths.asset_types.put import ApiForput
from eliona.api_client.paths.asset_types.post import ApiForpost


class AssetTypes(
    ApiForget,
    ApiForput,
    ApiForpost,
):
    pass
