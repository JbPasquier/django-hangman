from django.conf.urls import url
from django.contrib import admin
from views import todo_list, todo_detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/todos/$', todo_list),
    url(r'^api/todos/(?P<id>[0-9]+)$', todo_detail),
    url(r'^$', todo_list),
]
