from django.shortcuts import render
from .forms import productForm,productnewForm
from django.http import HttpResponse
from django.contrib import messages
from .models import productnew
# Create your views here.


def admin(request):

	#return HttpResponse("Hello");
	

	return render(request,'cart/admin.html');

def index(request):

	allproducts = productnew.objects.all()
	#del request.session['cart']
	if 'jcart22' in request.session:

		cart = request.session['jcart22']
	else:

		cart = ""

	if 'count22' in request.session:
		count = request.session['count22']
	else:
		count=0
	if 'total22' in request.session:
		total = request.session['total22']
	else:
		total=0
	
	return render(request,'cart/index.html',{'allproducts':allproducts,'count':count,'myString':cart,'total':total});

def uploadform(request):
	forms = productnewForm

	if request.method=="GET":

		
		return render(request,'cart/admin.html',{'forms':forms});

	if request.method=="POST":

		forms = productnewForm(request.POST,request.FILES)
		if forms.is_valid():

			productnew = forms.save(commit=False)
			

			forms.save()
			messages = "Uploading Was Successful"

			return render(request,'cart/admin.html',{'messages':messages});

def viewproduct(request):

	products = productnew.objects.all()

	return render(request,'cart/admin.html',{'products':products})


def deleteproduct(request):

	if request.is_ajax() or request.POST:


	#if request.method =="POST":
		pname = request.POST['pname']

		query= productnew.objects.get(productname=pname)
		query.delete()
		

		return HttpResponse("deleted")
def list_duplicates(seq):

	seen = set()
	seen_add = seen.add()

	seen_twice = set(x for x in seq if x in seen or seen_add(x))

	return list(seen_twice)
		

def cartproduct(request):
	
	if request.is_ajax() or request.POST:
		
		use =""
		pname = request.POST['pname']
		price = request.POST['price']
		img = request.POST['img']
		quantity = request.POST['quantity']
		#array1 = [{'pname':pname,'price':price,'img':img}]
		arr = [pname,price,quantity,img]
		already = []
		
	if 'jcart22' not in request.session:
		request.session['jcart22'] = []
		cart_list = request.session['jcart22']
		cart_list.append(arr)
		request.session['jcart22'] = cart_list
		request.session['count22'] = 1
		
		

	else:
		
		
		#uniq = []
		cart_list = request.session['jcart22']

		count = request.session['count22']

		

		#user = set([pname for pname in cart_list if cart_list.count(pname) > 1])
		#for c_list in enumerate(cart_list):
			#if pname in c_list:
		if count > 0:
			a = [1,2,3,4,2,3,5,6,7,7,7,7,7,7,8]

        	


			for i in range(count):
				if pname in cart_list[i][0]:
					already.append(cart_list[i][0])
        	
        		
				if len(already) > 0:
					use="Item Already Picked....quantity updated"
					x = int(cart_list[i][2]) + 1
					cart_list[i][2] = x
					
					request.session['jcart22'] = cart_list
					#request.session['count22']=count

				


			
		if count <= 0:

			cart_list.append(arr)
			count +=1
			
			request.session['jcart22'] = cart_list
			request.session['count22'] = count
			

		if use != "Item Already Picked....quantity updated":
		

			cart_list.append(arr)
			count +=1
			
			request.session['jcart22'] = cart_list
			request.session['count22'] = count
			

		


			#[x for x,y in d.items() if y > 1]
				#user = "Already"
		
				#uniq.append(c_list)
			
	return HttpResponse(use)


def cartitem(request):

	if 'jcart22' in request.session:

		cart = request.session['jcart22']
		count = request.session['count22']
		sumtotal = 0
		add=[]
		for i in range(count):

			quantity = int(cart[i][1]) * int(cart[i][2]) 

			sumtotal +=quantity
			add.append(quantity)




	return render(request ,'cart/cartItem.html',{'myString':cart,'sumtotal':sumtotal})

def multiply(value, arg):
	return value*arg

def updatecart(request):

	if request.is_ajax() or request.POST:

		pname = request.POST['pname']
		update = request.POST['update']

		if 'jcart22' in request.session:

			cart_list = request.session['jcart22']

			count = request.session['count22']
			

			for i in xrange(count):

				if pname in cart_list[i][0]:
					
					cart_list[i][2] = update
					request.session['jcart22'] = cart_list

			

		return HttpResponse("ok")
