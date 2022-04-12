from django.urls import path, re_path
from blog import views

app_name='blog'
urlpatterns=[
    path('',PostLV.as_view(), name='index'),
    path('post/', views.PostLV.as_view(), name='post_list'),
    re_path(r'^post/(?P<slug>[-\w]+)/$',views.PostDV.as_view(), name='post_detail'),
    path('archieve/',views.PostAV.as_view(), name='psot_archieve'),
    path('archieve/<int:year>/',views.PostYAV.as_view(), name='post_year_archieve'),
    path('archieve/<int:year>/<str:month>/',views.PostMAV.as_view(), name='post_month_archieve'),
    path('archieve/<int:year>/<str:month>/<int:day>/',views.PostDAV.as_view(), name='post_day_archieve'),
    path('archieve/today/',views.PostTAV.as_view(), name='post_today_archieve'),
]
