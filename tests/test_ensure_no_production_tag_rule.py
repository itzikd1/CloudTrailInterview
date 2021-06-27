import unittest

from cloudrail.dev_tools.rule_test_utils import create_empty_entity
from cloudrail.knowledge.context.aws.aws_environment_context import AwsEnvironmentContext
from cloudrail.knowledge.context.aws.ec2.ec2_instance import Ec2Instance
from cloudrail.knowledge.rules.base_rule import RuleResultType

from cloudrail.rules.ensure_no_production_tag_rule import EnsureNoProductionTagRule


class TestEnsureAllResourcesTaggedRule(unittest.TestCase):
    def setUp(self):
        self.rule = EnsureNoProductionTagRule()

    def test_production_tag_exist_fail(self):
        # Arrange
        ec2: Ec2Instance = create_empty_entity(Ec2Instance)
        tags = {'name': 'ec2_instance', 'environment': 'production'}
        ec2.tags = tags
        context = AwsEnvironmentContext(ec2s=[ec2])
        # Act
        result = self.rule.run(context, {})
        # Assert
        self.assertEqual(RuleResultType.FAILED, result.status)
        self.assertEqual(1, len(result.issues))

    def test_production_not_tag_exist_pass(self):
        # Arrange
        ec2: Ec2Instance = create_empty_entity(Ec2Instance)
        tags = {'name': 'ec2_instance', 'environment': 'develop'}
        ec2.tags = tags
        context = AwsEnvironmentContext(ec2s=[ec2])
        # Act
        result = self.rule.run(context, {})
        # Assert
        self.assertEqual(RuleResultType.SUCCESS, result.status)
        self.assertEqual(0, len(result.issues))
