from django.shortcuts import render, get_object_or_404, redirect
from GOODS.models import  Info

def info_list(request):
    infos = Info.objects.all()
    return render(request, 'info_list.html', {'infos': infos})

def info_detail(request, id):
    info = get_object_or_404(Info, id=id)
    return render(request, 'info_detail.html', {'info': info})

def info_create(request):
    if request.method == "POST":
        phone_number = request.POST['phone_number']
        location = request.POST['location']
        email = request.POST['email']
        info = Info(phone_number=phone_number, location=location, email=email)
        info.save()
        return redirect('info_detail', pk=info.pk)
    return render(request, 'info_form.html')

def info_update(request, id):
    info = get_object_or_404(Info, id=id)
    if request.method == "POST":
        info.phone_number = request.POST['phone_number']
        info.location = request.POST['location']
        info.email = request.POST['email']
        info.save()
        return redirect('info_detail', pk=info.pk)
    return render(request, 'info_form.html', {'info': info})

def info_delete(request, id):
    info = get_object_or_404(Info, id=id)
    if request.method == "POST":
        info.delete()
        return redirect('info_list')
    return render(request, 'info_confirm_delete.html', {'info': info})
