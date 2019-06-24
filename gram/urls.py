from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
urlpatterns=[
    url('home/', PostListView.as_view(), name='welcome'),
    url('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    url('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    url('post/new/', PostCreateView.as_view(), name='post-create'),
    url('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    url('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # url('about/', views.about, name='Insta-about'),
    url('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),


    # url('^$',views.home,name = 'welcome'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)