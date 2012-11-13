from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from simpleBlog.models import Post

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Post.objects.order_by('-pub_date')[:5],
            context_object_name='latest_post_list',
            template_name='simpleBlog/index.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Post,
            template_name='simpleBlog/detail.html'),
        name='post_detail'),

    url(r'^(today)/',  
        ListView.as_view(
            queryset=Post.objects.order_by('-pub_date'),
            paginate_by=5,
            context_object_name='posts_to_check',
            template_name='simpleBlog/today.html')),

    url(r'^(month)/',  
        ListView.as_view(
            queryset=Post.objects.order_by('-pub_date'),
            paginate_by=5,
            context_object_name='posts_to_check',
            template_name='simpleBlog/month.html')),

    url(r'^(year)/',  
        ListView.as_view(
            queryset=Post.objects.order_by('-pub_date'),
            paginate_by=5,
            context_object_name='posts_to_check',
            template_name='simpleBlog/year.html')),


    url(r'^(?P<post_id>\d+)/vote/$', 'simpleBlog.views.vote'),
    url(r'^(?P<post_id>\d+)/comment/$', 'simpleBlog.views.comment', name='post_comment'),
)