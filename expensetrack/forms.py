from django.forms import ModelForm
from .models import Expensetrack_expense

class Expensetrack_expense_Form(ModelForm):
    class Meta:
        model = Expensetrack_expense
        fields = '__all__'