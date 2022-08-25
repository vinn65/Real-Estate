from django.shortcuts import render, redirect 
from django.contrib import messages
from . models import property
from . forms import UserRegistrationForm, PropertyRegistrationform
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'base/nav.html')


def Property(request):
    properties = property.objects.filter(owner=request.user)
    property_count = properties.count()
    context = {
        'properties':properties,'property_count':property_count
    }
    return render(request, 'base/property.html',context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f" Hey {username}! Your Account has been Created!!")
            return redirect('login')
    else:           
        form = UserRegistrationForm()
    context = {
            "form":form
        }
    return render(request,'base/register.html',context)    

def Registerproperty(request):
    form = PropertyRegistrationform()
    if request.method == 'POST':
        property.objects.create(
            owner = request.user,
            description = request.POST.get('description'),
            location = request.POST.get('location'),
            city = request.POST.get('city'),
            price = request.POST.get('price'),
            image = request.POST.get('image'),
            type = request.POST.get('type'),
            status = request.POST.get('status'),
        )
        return redirect('property')
    context = {
        'form':form
    }
    return render(request,'base/propertyreg.html',context)

def PropertySearch(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # properties  = property.objects.all()
    properties = property.objects.filter(
        # Q(type__name__contains = q) |
        Q(price__icontains = q) |
        Q(status__icontains = q) |
        Q(description__icontains = q) |
        Q(location__icontains = q) |
        Q(city__icontains = q) 

    )
    context = {
        'properties':properties
    }
    return render(request, 'base/search.html',context)

def contact(request):
    return render(request, 'base/contact.html')

def View(request):
    properties = property.objects.filter(owner=request.user)
    property_count = properties.count()
    context = {
        'properties':properties,'property_count':property_count
    }
    return render(request, 'base/view.html',context)

def update_property(request,pk):
    prop = property.objects.get(id=pk)
    form = PropertyRegistrationform()
    # topics = Topic.objects.all()
    if request.method == 'POST':
        prop.owner = request.user,
        prop.description = request.POST.get('description'),
        prop.location = request.POST.get('location'),
        prop.city = request.POST.get('city'),
        prop.price = request.POST.get('price'),
        prop.image = request.POST.get('image'),
        prop.type = request.POST.get('type'),
        prop.status = request.POST.get('status'),
        prop.save()
        
        return redirect('property')
 
    context = {'form':form,'prop':prop}
    return  render(request,'base/propertyreg.html', context)

def delete_property(request,pk):
    prop = property.objects.get(id=pk)
    if request.method == 'POST':
        prop.delete()
        return redirect('property')

    return render(request, 'base/delete.html', {'obj':prop})