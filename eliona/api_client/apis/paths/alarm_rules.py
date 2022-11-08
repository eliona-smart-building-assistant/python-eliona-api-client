from eliona.api_client.paths.alarm_rules.get import ApiForget
from eliona.api_client.paths.alarm_rules.put import ApiForput
from eliona.api_client.paths.alarm_rules.post import ApiForpost


class AlarmRules(
    ApiForget,
    ApiForput,
    ApiForpost,
):
    pass
