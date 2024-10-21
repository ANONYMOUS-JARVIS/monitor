from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .utils import create_rule, combine_rules, evaluate_rule
from .models import ASTNode


def create_rule_view(request):
    ast_id = None
    if request.method == 'POST':
        rule_string = request.POST.get('rule_string')
        ast = create_rule(rule_string)
        ast_id = ast.id
    return render(request, 'create_rule.html', {'ast_id': ast_id})

def combine_rules_view(request):
    combined_ast_id = None
    if request.method == 'POST':
        rules = request.POST.getlist('rules')
        combined_ast = combine_rules(rules)
        combined_ast_id = combined_ast.id
    return render(request, 'combine_rules.html', {'combined_ast_id': combined_ast_id})

def evaluate_rule_view(request):
    result = None
    if request.method == 'POST':
        ast_id = request.POST.get('ast_id')
        data = request.POST.get('data')
        ast = ASTNode.objects.get(id=ast_id)
        result = evaluate_rule(ast, data)
    return render(request, 'evaluate_rule.html', {'result': result})


