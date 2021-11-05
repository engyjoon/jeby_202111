from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='common:login')
def news_list(request):
    """
    뉴스 리스트를 반환한다.
    """
    return render(
        request,
        'news/news_list.html',
    )