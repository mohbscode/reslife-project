from django.shortcuts import render

# Create your views here.
def all_storage(request):
    return render(request, 'storage/all_storage.html')
