import unittest

from cloudrail.dev_tools.rule_test_utils import create_empty_entity
from cloudrail.knowledge.context.aws.aws_environment_context import AwsEnvironmentContext
from cloudrail.knowledge.context.aws.ec2.ec2_instance import Ec2Instance
from cloudrail.knowledge.rules.base_rule import RuleResultType

from cloudrail.rules.ensure_there_are_no_ec2_with_similar_names_rule import EnsureThereAreNoEc2WithSimilarNamesRule


class TestEnsureThereAreNoEc2WithSimilarNamesRule(unittest.TestCase):
    def setUp(self):
        self.rule = EnsureThereAreNoEc2WithSimilarNamesRule()

    def test_are_not_similar_fail(self):
        # Arrange
        ec2_1: Ec2Instance = create_empty_entity(Ec2Instance)
        ec2_1.name = 'cat'
        ec2_2: Ec2Instance = create_empty_entity(Ec2Instance)
        ec2_2.name = 'dog'
        context = AwsEnvironmentContext(ec2s=[ec2_1, ec2_2])
        # Act
        result = self.rule.run(context, {})
        # Assert
        self.assertEqual(RuleResultType.FAILED, result.status)
        self.assertEqual(1, len(result.issues))

    def test_are_similar_pass(self):
        # Arrange
        ec2_1: Ec2Instance = create_empty_entity(Ec2Instance)
        ec2_1.name = 'god'
        ec2_2: Ec2Instance = create_empty_entity(Ec2Instance)
        ec2_2.name = 'good'
        context = AwsEnvironmentContext(ec2s=[ec2_1, ec2_2])
        # Act
        result = self.rule.run(context, {})
        # Assert
        self.assertEqual(RuleResultType.SUCCESS, result.status)
        self.assertEqual(0, len(result.issues))
