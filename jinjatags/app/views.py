from django.shortcuts import render

# Create your views here.
def print(request):
    d={'name':'something'}
    return render(request,'print.html',context=d)





def operation(request):
    d={'name':'something','age':22}
    return render(request,'operation.html',context=d)
