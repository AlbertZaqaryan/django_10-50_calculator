from django.shortcuts import render

# Create your views here.

def calculator(request):
    number1 = request.POST.get('number1')
    char = request.POST.get('char')
    number2 = request.POST.get('number2')
    res = 0
    if char == '+':
        res = int(number1) + int(number2)
    elif char == '-':
        res = int(number1) - int(number2)
    elif char == '*':
        res = int(number1) * int(number2)
    elif char == '/':
        try:
            res = int(number1) / int(number2)
        except ZeroDivisionError:
            res = 'No 0 :( !!!!'
            return render(request, 'main/calculator.html', context={'res':res})
    return render(request, 'main/calculator.html', context={'res':res})
    