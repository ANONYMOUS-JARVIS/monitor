from .models import ASTNode

def create_rule(rule_string):
    # Implement a simple parser to convert the rule string to AST.
    # This is a basic approach, but you'll need to add a real parser.
    # Example: parse "age > 30" into an ASTNode

    # Assuming you use an external parsing library to convert the string to AST.
    # Example pseudo-code
    root = ASTNode.objects.create(type='operator', value='AND')
    left_operand = ASTNode.objects.create(type='operand', value='age > 30')
    right_operand = ASTNode.objects.create(type='operand', value="department = 'Sales'")
    
    root.left = left_operand
    root.right = right_operand
    root.save()

    return root
def combine_rules(rules):
    # Logic to combine multiple AST trees.
    # Combine using a common operator such as 'AND' or 'OR'
    root = ASTNode.objects.create(type='operator', value='AND')
    
    for rule in rules:
        # You can create sub-trees for each rule and combine them under the root
        sub_tree = create_rule(rule)
        # Attach sub_tree under the root (extend as needed)
        root.left = sub_tree  # Simplification; handle left/right child accordingly
    
    root.save()
    return root
def evaluate_rule(ast, data):
    if ast.type == 'operand':
        # Evaluate the operand (for example, 'age > 30')
        return eval_operand(ast.value, data)
    elif ast.type == 'operator':
        # Recursively evaluate the left and right children
        left_result = evaluate_rule(ast.left, data)
        right_result = evaluate_rule(ast.right, data)

        if ast.value == 'AND':
            return left_result and right_result
        elif ast.value == 'OR':
            return left_result or right_result

def eval_operand(condition, data):
    # Parse the condition, e.g., 'age > 30', and compare it with the data
    # Example: "age > 30" should become `data["age"] > 30`
    # This is a simplified evaluation; you'll need to parse properly
    field, operator, value = parse_condition(condition)  # Custom parser needed
    return eval(f'{data[field]} {operator} {value}')
