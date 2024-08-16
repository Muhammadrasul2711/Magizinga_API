from django.shortcuts import render, get_object_or_404, redirect
from Goods.models import Banner


def banner_list(request):
    banners = Banner.objects.all()
    return render(request, 'back-office/Banner/banner_list.html', {'banners': banners})


def banner_detail(request, id):
    banner = get_object_or_404(Banner, id=id)
    return render(request, 'back-office/Banner/banner_detail.html', {'banner': banner})


def banner_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        sub_title = request.POST.get('sub_title')
        img = request.FILES.get('img')
        is_active = request.POST.get('is_active') == 'on'

        banner = Banner(title=title, sub_title=sub_title, img=img, is_active=is_active)
        banner.save()
        return redirect('banner_detail', id=banner.id)
    return render(request, 'back-office/Banner/BannerForm.html')


def banner_update(request, id):
    banner = get_object_or_404(Banner, id=id)
    if request.method == "POST":
        banner.title = request.POST.get('title')
        banner.sub_title = request.POST.get('sub_title')
        if request.FILES.get('img'):
            banner.img = request.FILES.get('img')
        banner.is_active = request.POST.get('is_active') == 'on'

        banner.save()
        return redirect('banner_detail', id=banner.id)
    return render(request, 'back-office/Banner/BannerForm.html', {'banner': banner})


def banner_delete(request, id):
    banner = get_object_or_404(Banner, id=id)
    if request.method == "POST":
        banner.delete()
        return redirect('banner_list')
    return render(request, 'back-ofice/Banner/banner_delled.html', {'banner': banner})
