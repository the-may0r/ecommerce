from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Merch
from .forms import NewMerchForm, EditMerchForm

# Create your views here.

def search(request):
    query = request.GET.get('query', '')
    items = Merch.objects.filter(is_sold=False)
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'merch.html', {
        'items': items,
        'query': query,
    })



def detail(request, pk):
    item = get_object_or_404(Merch, pk=pk)
    related_items = Merch.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]


    return render(request, 'detail.html', {
        'item':item,
        'related_items':related_items,
        })


@login_required
def new(request):
    if request.method == 'POST':
        form = NewMerchForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('detail', pk=item.id)

    else:
        form = NewMerchForm()

    return render(request, 'form.html', {
        'form': form,
        'title': 'New merch',
    })


@login_required
def edit_item(request, pk):
    item = get_object_or_404(Merch, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditMerchForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            item.save()
            return redirect('detail', pk=item.id)

    else:
        form = EditMerchForm(instance=item)

    return render(request, 'form.html', {
        'form': form,
        'title': 'Edit merch',
    })

@login_required
def delete_item(request, pk):
    item = get_object_or_404(Merch, pk=pk, created_by=request.user)
    item.delete()

    return redirect('index_dash')
