from typing import Dict, List
import nltk
from cloudrail.knowledge.context.aws.aws_environment_context import AwsEnvironmentContext
from cloudrail.knowledge.rules.aws.aws_base_rule import AwsBaseRule
from cloudrail.knowledge.rules.base_rule import Issue
from cloudrail.knowledge.rules.rule_parameters.base_paramerter import ParameterType


class EnsureThereAreNoEc2WithSimilarNamesRule(AwsBaseRule):
    def execute(self, env_context: AwsEnvironmentContext, parameters: Dict[ParameterType, any]) -> List[Issue]:
        issues: List[Issue] = []
        instance1 = (env_context.ec2s[0])
        name1 = instance1.name
        instance2 = (env_context.ec2s[1])
        name2 = instance2.name
        if nltk.edit_distance(name1, name2) > 1:
            new_issue = Issue(instance1.get_id(), "true", "true")
            issues.append(new_issue)
        return issues

    def get_id(self) -> str:
        return 'ensure_there_are_no_ec2_with_similar_names_rule'

    def should_run_rule(self, environment_context: AwsEnvironmentContext) -> bool:
        return True
