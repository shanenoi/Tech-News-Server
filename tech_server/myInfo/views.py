from django.http import HttpResponse
from django.shortcuts import render
from info.my_info import Danh


def info(request):
    return render(
        request,
        "myInfo/base.html",
        {"my":Danh}
    )