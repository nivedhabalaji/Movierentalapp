from django.shortcuts import render,redirect
# Create your views here.
from .models import Customers,Movies

from .forms import customerp,moviep


def homepage(request):
	return render(request,'home.html',context=None)

def addcustomer(request):
	if request.method=="POST":
		form=customerp(request.POST)
		if form.is_valid():
			firstname=form.cleaned_data['firstname']
			lastname=form.cleaned_data['lastname']
			email=form.cleaned_data['email']
			contact=form.cleaned_data['contact']
			address=form.cleaned_data['address']
			city=form.cleaned_data['city']
			state=form.cleaned_data['state']
			zipcode=form.cleaned_data['zipcode']
			country=form.cleaned_data['country']
			info_obj=Customers(firstname=firstname,lastname=lastname,email=email,contact=contact,address=address,city=city,state=state,zipcode=zipcode,country=country)
			info_obj.save()
		return redirect("/movie/listcustomers/")
	else:

		form=customerp(None)
		return render(request,'customer.html',{'form':form})
		

def addmovie(request):
 	if request.method=="POST":
 		form=moviep(request.POST)
 		if form.is_valid():
 			moviename=form.cleaned_data['moviename']
 			category=form.cleaned_data['category']
 			price=form.cleaned_data['price']
 			info_obj=Movies(moviename=moviename,category=category,price=price)
 			info_obj.save()
 			return redirect("/movie/availablemovies/")
 	else:

 		form=moviep()
 		return render(request,'movie.html',{'form':form})

def availablemovies(request):
	avail_filter=Movies.objects.filter(customer__isnull=True)
	return render(request,'table.html',{'avail':avail_filter})

def rentedmovies(request):
	remove_rented=Movies.objects.filter(customer__isnull=False)
	if request.method=='POST':
		id2=int(request.POST.get('return'))
		filtering = Movies.objects.filter(id=id2).update(customer=None)
	return render(request,'rented.html',{'fil':remove_rented})

def listcustomers(request):
	return render(request,'lists.html',{'customers':Customers.objects.all()})

def assignmovie(request):
	a=Movies.objects.all()
	b=Customers.objects.all()
	cus=request.POST.get('customer_data')
	mov=request.POST.get('movie_data')
	if request.method=='POST':
		d=Movies.objects.get(moviename=mov)
		e=Customers.objects.get(firstname=cus)
		d.customer=e
		d.save()

	return render(request,'assign.html',{'movies':a, 'customers':b})

def delete(request,deleteid):
	if request.method=='POST':
		d=Movies.objects.filter(id=deleteid)
		d.delete()
	return redirect('/movie/availablemovies/')