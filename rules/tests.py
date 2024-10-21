from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import ASTNode
from rules.views import create_rule, evaluate_rule

class RuleEngineTestCase(TestCase):
    def test_create_rule(self):
        rule_string = "(age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')"
        root_node = create_rule(rule_string)
        
        # Test if the root node is an OR operator
        self.assertEqual(root_node.type, 'operator')
        self.assertEqual(root_node.value, 'OR')

        # Test if the left child is an AND node
        self.assertEqual(root_node.left.type, 'operator')
        self.assertEqual(root_node.left.value, 'AND')

        # Test the first condition in the AST (age > 30)
        self.assertEqual(root_node.left.left.value['left'], 'age')
        self.assertEqual(root_node.left.left.value['operator'], '>')
        self.assertEqual(root_node.left.left.value['right'], '30')

        # Add more assertions as needed for the entire AST structure
class RuleEngineEvaluationTestCase(TestCase):
    def test_evaluate_rule(self):
        rule_string = "(age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')"
        root_node = create_rule(rule_string)

        # Define sample data for testing
        sample_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
        
        # Test if the rule evaluates to True
        result = evaluate_rule(root_node, sample_data)
        self.assertTrue(result)

        # Test a different set of data
        sample_data = {"age": 40, "department": "Marketing", "salary": 30000, "experience": 5}
        result = evaluate_rule(root_node, sample_data)
        self.assertTrue(result)

        # Test when the rule should evaluate to False
        sample_data = {"age": 20, "department": "IT", "salary": 40000, "experience": 2}
        result = evaluate_rule(root_node, sample_data)
        self.assertFalse(result)

