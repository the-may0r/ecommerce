from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from merch.models import Merch

# Create your views here.
@login_required
def index_dash(request):
    items = Merch.objects.filter(created_by=request.user)

    return render(request, 'dashboard.html', {
        'items': items,
    })