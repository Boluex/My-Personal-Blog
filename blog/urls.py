from django.urls import path,include
from.import views
# from .api import views as api_view
urlpatterns =[
    path('',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('about/',views.about,name='about'),
    path('add_comment/<int:id>',views.add_comment,name='add_comment'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('destroy/<int:id>',views.destroy,name='destroy'),
    path('new_update/<int:id>',views.new_update,name='updates'),
    path('comment/<int:id>',views.comments,name='comment'),

    # #rest_framework urls
    # path('api_detail/<int:id>', api_view.api_detail, name='api_detail'),
    # path('api_update/<int:id>', api_view.api_update, name='api_update'),
    # path('api_delete/<int:id>', api_view.api_delete, name='api_delete'),
    # path('api_home/', api_view.api_home.as_view(), name='api_home'),
    # path('api_create/', api_view.api_create, name='api_create'),
]