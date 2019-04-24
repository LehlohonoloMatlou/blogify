from django.conf.urls import url, include

from blogify import views

urlpatterns =[
	#view list urls
	url(r'^audiences/',views.view_audiences,name='view_audiences'),
	url(r'^articles/',views.view_articles,name='view_articles'),
	url(r'^$',views.view_articles,name=''),

	#view single object urls
	url(r'^audience/(\d+)/$',views.view_audience,name = 'view_audience'),
	url(r'^article/(\d+)/$',views.view_article,name='view_article'),

	#add object urls
	url(r'^add_audience/',views.add_audience,name='add_audience'),
	url(r'^add_article/',views.add_article,name='add_article'),

	#update object urls
	url(r'^update_audience/(\d+)/',views.update_audience,name='update_audience'),
	url(r'^update_article/(\d+)/',views.update_article,name='update_article'),

	#delete object urls
	url(r'^delete_audience/(\d+)/',views.delete_audience,name='delete_audience'),
	url(r'^delete_article/(\d+)/',views.delete_article,name='delete_article'),
]