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
        form = ProductForm(request.form)
        if form .is_valid():
            form.save()
            return ridirect ('product_list')
    return render(request, 'invApp/product_form.html', {'form':form})
    
#Read View 
def product_list_view(request):
    product = products.objects.all()
    return render(request, 'InvApp/product_list.html', {'products':product})

#Update View 
def product_update_view(request):
    product.objects.get(product_id=product_id )
    form = ProductForm(instance = product)
    if request.method == "POST":
        ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form':form})

#Delete View 
def product_delete_view(request, product_id):
    product.objects.get(product_id=product_id )
    form = ProductForm(instance = product)
    if request.method == "POST":
        Product.delete()
        return redirect('product_list')
    
    return render (request, 'invApp/product_comfirm_delete.html', {'products':product})
