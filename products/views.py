from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import JsonResponse
from .models import Product

from django.utils import timezone


# Create your views here.
@login_required(login_url="/accounts/signup")
def create(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['tel_number'] and request.POST['description'] and request.POST['address'] and request.FILES['images'] and request.POST['price']:
			product = Product()
			product.title = request.POST['title']
			product.tel_number = request.POST['tel_number']
			product.description = request.POST['description']
			product.images = request.FILES['images']
			product.pub_date = timezone.datetime.now()
			product.price = request.POST['price']
			product.address = request.POST['address']
			product.hunter = request.user
			product.save()
			return redirect('userroom')
		else:
			return render(request, 'create.html', {'error': 'All Fields are required'})
	else:
		return render(request, 'create.html')

        

def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'detail.html', {'product':product})

@login_required(login_url="/accounts/signup")
def stars(request, product_id):
	if request.method == 'POST':
		product = get_object_or_404(Product, pk=product_id)
		product.stars += 1
		product.save()
		return redirect('home')

@login_required(login_url="/accounts/signup")
def user_room(request):
	sorted_product = Product.objects.filter(hunter=request.user)
	return render(request, 'user_room.html', {'sorted_product': sorted_product})

@login_required(login_url="/accounts/signup")
def delete(request, product_id):
	delete_product = get_object_or_404(Product, pk=product_id)
	delete_product.delete()
	sorted_product = Product.objects.filter(hunter=request.user)
	return render(request, 'user_room.html', {'sorted_product': sorted_product})

@login_required(login_url="/accounts/signup")
def modify(request, product_id):
	modify_product = get_object_or_404(Product, pk=product_id)
	if request.method == 'POST':
		modify_product.title = request.POST['title']
		modify_product.tel_number = request.POST['tel_number']
		modify_product.description = request.POST['description']
		modify_product.pub_date = timezone.datetime.now()
		modify_product.price = request.POST['price']
		modify_product.address = request.POST['address']
		modify_product.save()
		

		
		return redirect('userroom')
	return render(request, 'modify.html', {'modify_product': modify_product})