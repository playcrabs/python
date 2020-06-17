from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Notice
from .customPager import CustomPager

# Create your views here.

def list(request, page=1, kind="title", search=""):
    # querySet
    # notice = Notice.objects.all() #select * from notice

    # slicing
    # start = (page-1)*2
    # last = page*2
    # notice = Notice.objects.order_by("-num")[start:last] #select * from notice order by num desc

    # paginator----------------------------------------
    # notice = Notice.objects.order_by("-num")
    # Paginator(Queryset, 갯수)
    # notice = Paginator(notice, 2)
    # 실제 조회
    # notice = notice.get_page(page)

    #CustomPager---------------------------------------
    customPager = CustomPager(page, kind, search)

    notice = Notice.objects.order_by("-num")
    notice = Paginator(notice, 2)

    customPager.makePage(notice.num_pages)

    notice = notice.get_page(customPager.page)


    context = {"board":"NoticeList", "list":notice, "pager":customPager,}

    return render(request, 'notice/list.html', context)