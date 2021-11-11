from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ..models import Keyword
from ..forms import NewsSearchForm
from ..utils import naverapi_utils as naverapi


@login_required(login_url="common:login")
def index(request):
    """
    뉴스 검색 화면으로 리다이렉트한다.
    """
    return redirect("news:news_search")


@login_required(login_url="common:login")
def news_search(request):
    """
    뉴스 검색 화면을 반환한다.
    """

    news_list = []
    keywords = Keyword.objects.all()

    if request.method == "POST":
        form = NewsSearchForm(request.POST)

        if form.is_valid():
            keyword = form.cleaned_data["keyword"]
            news_list = naverapi.get_news_by_hour(keyword)
    else:
        form = NewsSearchForm()

    return render(
        request,
        "news/news_search.html",
        {"form": form, "news_list": news_list, "keywords": keywords},
    )
