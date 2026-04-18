from django.shortcuts import render, redirect

from .forms import ProductForm
from .models import product

# Create your views here.
#CRUD = Create, Read, Update, Delete

#Create View 
def home_view(request):
    return render(request, 'invApp/home.html')

#Home Iview
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form .is_valid():
            form.save()
            return redirect ('product_list')
    return render(request, 'invApp/product_form.html', {'form':form})
    
#Read View 
def product_list_view(request):
    products = product.objects.all()
    return render(request, 'InvApp/product_list.html', {'products':products})

#Update View 
# 1. Add 'product_id' as a parameter
def product_update_view(request, product_id):
    # 2. Assign the result of the query to a variable named 'obj'
    obj = product.objects.get(product_id=product_id)
    
    # 3. Use 'obj' as the instance for your form
    form = ProductForm(instance=obj)
    
    if request.method == "POST":
        form = ProductForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('product_list')
            
    return render(request, 'invApp/product_form.html', {'form': form})

#Delete View 
def product_delete_view(request, product_id):
    obj = product.objects.get(product_id=product_id)
    if request.method == "POST":
        obj.delete()
        return redirect('product_list')
    
    return render (request, 'invApp/product_comfirm_delete.html', {'products':product})
