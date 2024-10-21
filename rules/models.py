
from django.db import models

class ASTNode(models.Model):
    TYPE_CHOICES = [
        ('operator', 'Operator'),
        ('operand', 'Operand'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    left = models.ForeignKey('self', on_delete=models.CASCADE, related_name='left_child', null=True, blank=True)
    right = models.ForeignKey('self', on_delete=models.CASCADE, related_name='right_child', null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return f'{self.type} - {self.value}'
