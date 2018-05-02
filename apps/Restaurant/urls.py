from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', RestaurantCreateListView.as_view(), name='create_list'),
    url(r'^(?P<pk>[0-9]+)/$', RestaurantUpdateView.as_view(), name='update'),
    url(r'^category/$', CategoryCreateListView.as_view()),
    url(r'^category/(?P<pk>[0-9]+)/', CategoryUpdateView.as_view()),
    url(r'^product/$', ProductCreateListView.as_view()),
    url(r'^product/(?P<pk>[0-9]+)/', ProductUpdateView.as_view()),
    url(r'^details/$', DetailsCreateListView.as_view()),
    url(r'^details/(?P<pk>[0-9]+)/', DetailsUpdateView.as_view()),
]