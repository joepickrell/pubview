from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from pubview import views
from pubview.models import Vote, Paper

urlpatterns = patterns('',
    url(r'^$',
	ListView.as_view(
		queryset=Paper.objects.order_by('-year')[:5],
		context_object_name='latest_paper_list',
		template_name='pubview/index.html'),
	name = 'index'),
    url(r'^(?P<pk>\d+)/$',
	DetailView.as_view(
		model = Paper,
		template_name = 'pubview/detail.html'),
	 name='detail'),
    url(r'^(?P<paper_id>\d+)/vote/$', views.vote, name='vote'),
)

