
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_pagination_data_ListView(page_obj, paginator, around_count=5):
    current_page = page_obj.number
    num_pages = paginator.num_pages

    left_has_more = False
    right_has_more = False
    left_more_page = 1
    right_more_page = num_pages

    if current_page <= around_count + 2:
        left_pages = range(1, current_page)
    else:
        left_has_more = True
        left_more_page = current_page - around_count - 1
        left_pages = range(current_page - around_count, current_page)
    if current_page >= num_pages - around_count - 1:
        right_pages = range(current_page + 1, num_pages + 1)
    else:
        right_has_more = True
        right_more_page = current_page + around_count + 1
        right_pages = range(current_page + 1, current_page + around_count + 1)

    return {
        'left_pages': left_pages,
        'right_pages': right_pages,
        'current_page': current_page,
        'left_has_more': left_has_more,
        'right_has_more': right_has_more,
        'num_pages': num_pages,
        'left_more_page': left_more_page,
        'right_more_page': right_more_page,
        'around_count': around_count,
    }

def get_pagination_data(page,list_name,paginator,around_count=5):
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    num_pages = page_obj.paginator.num_pages
    current_page=page_obj.number

    left_has_more = False
    right_has_more = False
    left_more_page = 1
    right_more_page = num_pages

    if current_page <= around_count + 2:
        left_pages = range(1, current_page)
    else:
        left_has_more = True
        left_more_page = current_page - around_count - 1
        left_pages = range(current_page - around_count, current_page)
    if current_page >= num_pages - around_count - 1:
        right_pages = range(current_page + 1, num_pages + 1)
    else:
        right_has_more = True
        right_more_page = current_page + around_count + 1
        right_pages = range(current_page + 1, current_page + around_count + 1)
    return {
                        list_name: page_obj.object_list,
                        "page_obj": page_obj,
                        'left_pages': left_pages,
                        'right_pages': right_pages,
                        'current_page': current_page,
                        'left_has_more': left_has_more,
                        'right_has_more': right_has_more,
                        'num_pages': num_pages,
                        'left_more_page': left_more_page,
                        'right_more_page': right_more_page,
                        'around_count': around_count,
                  }