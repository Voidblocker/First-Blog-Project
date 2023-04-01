from django.urls import path
from .views import home_view,detail_view,form_create_view,tag_create_view,handle_author_form

urlpatterns = [
    path('', home_view , name = 'home'),
    path('post/<int:post_id>/', detail_view , name = 'detail'),
    path('form-process/' , form_create_view , name ='form'),
    path('tag-create/', tag_create_view, name ='tag'),
    path('author-create/', handle_author_form , name ='author-create')

]