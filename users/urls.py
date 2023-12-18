from django.urls import path
from.import views
# from.user_api import views as user_view
urlpatterns =[
    path('register/',views.register,name='register'),
    path('login/',views.sign_in,name='sign_in'),
    path('logout/',views.sign_out,name='sign_out'),
    path('profile/',views.profile,name='profile'),
    path('profile/<str:username> ',views.profile_post,name='profile_post'),
    path('update_profile/',views.update_profile,name='update_profile'),

    # path('login/',user_view.login),
]