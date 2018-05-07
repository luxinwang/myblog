from django import template
register = template.Library()
# 自定义过滤器
@register.filter
def kong_upper(val):
    # print ('val from template:',val)
    return val.upper()

 # 自定义标签
from django.utils.html import format_html
@register.simple_tag
def circle_page(curr_page,loop_page,url,where):

    offset = abs(curr_page - loop_page)
    if offset < 3:
        if curr_page == loop_page:
            page_ele = '<li class="am-active"><a href="%s%s?%s">%s</a></li>'%(url,loop_page,where,loop_page)
            # page_ele = str(loop_page)
        else:
            page_ele = '<li><a href="%s%s?%s">%s</a></li>'%(url,loop_page,where,loop_page)
            # page_ele = str(loop_page)
        return format_html(page_ele)
    else:
        return ''