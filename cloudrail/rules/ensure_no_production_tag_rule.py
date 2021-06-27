from typing import Dict, List

from cloudrail.knowledge.context.aws.aws_environment_context import AwsEnvironmentContext
from cloudrail.knowledge.rules.aws.aws_base_rule import AwsBaseRule
from cloudrail.knowledge.rules.base_rule import Issue
from cloudrail.knowledge.rules.rule_parameters.base_paramerter import ParameterType


class EnsureNoProductionTagRule(AwsBaseRule):
    def execute(self, env_context: AwsEnvironmentContext, parameters: Dict[ParameterType, any]) -> List[Issue]:
        issues: List[Issue] = []
        for env_instance in env_context.ec2s:
            if "environment" in env_instance.tags:
                if env_instance.tags['environment'] == "production":
                    new_issue = Issue(env_instance.get_id(), "true", "true")
                    issues.append(new_issue)
        return issues

    def get_id(self) -> str:
        return 'ensure_no_production_tag_rule'

    def should_run_rule(self, environment_context: AwsEnvironmentContext) -> bool:
        return True
