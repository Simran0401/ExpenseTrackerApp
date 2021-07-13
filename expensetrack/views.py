from django.shortcuts import render, redirect
from .models import Expensetrack_expense
from django.http import HttpResponse


# Create your views here.
# home
def home(request):
    expenses = Expensetrack_expense.objects.all()
    if request.POST:
        month = request.POST['month']
        year = request.POST['year']
        expenses = Expensetrack_expense.objects.filter(date__year=year, date__month=month)
    return render(request, 'index1.html', {'expenses': expenses})

# create
def add(request):
    if request.method == 'POST':
        item = request.POST['item']
        amount = request.POST['amount']
        category = request.POST['category']
        date = request.POST['date']

        expense = Expensetrack_expense(item=item, amount=amount, category=category, date=date)
        expense.save()

    return redirect(home)

def update(request, id):
    id = int(id)
    expense_fetched = Expensetrack_expense.objects.get(id = id)
    if request.method == 'POST':
        item = request.POST['item']
        amount = request.POST['amount']
        category = request.POST['category']
        date = request.POST['date']

        expense_fetched.item = item
        expense_fetched.amount = amount
        expense_fetched.category = category
        expense_fetched.date = date

        expense_fetched.save()

    return redirect(home)

def delete(request, id):
    id = int(id)
    expense_fetched = Expensetrack_expense.objects.get(id = id)
    expense_fetched.delete()
    return redirect(home)