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
            template_name='simpleBlog/detail.html')),

    # TODO: posts by from this month view
    # TODO: posts by from this year view
    # TODO: posts by from this day view 

    url(r'^(?P<post_id>\d+)/vote/$', 'simpleBlog.views.vote'),
)