from eliona.api_client.paths.aggregations_aggregation_id.get import ApiForget
from eliona.api_client.paths.aggregations_aggregation_id.put import ApiForput
from eliona.api_client.paths.aggregations_aggregation_id.delete import ApiFordelete


class AggregationsAggregationId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
