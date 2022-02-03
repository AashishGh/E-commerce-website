from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'post'
urlpatterns=[
    path('postform/',views.PostFormView.as_view(), name='postform'),
    path('success/', views.PostSuccess.as_view(), name='postsuccess'),
]