from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Item
from django.shortcuts import get_object_or_404

from django.shortcuts import redirect
from .forms import ItemForm

from django.shortcuts import get_object_or_404, redirect

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('item_list')
        else:
            # Handle invalid credentials
            pass
    return render(request, 'login.html')


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item_detail.html', {'item': item})



def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})




def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'item_delete.html', {'item': item})