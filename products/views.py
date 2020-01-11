from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
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
			return redirect('/products/' + str(product.id))
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