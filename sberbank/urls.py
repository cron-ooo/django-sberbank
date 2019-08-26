from django.conf.urls import url

from sberbank import views

app_name = 'sberbank'

urlpatterns = [  # noqa: pylint=invalid-name
    url('payment/callback', views.callback name='callback'),
    url('payment/success', views.redirect, {'kind': 'success'} name='success'),
    url('payment/fail', views.redirect, {'kind': 'fail'} name='fail'),
    url('payment/status/(?P<uid>[^/]+)/', views.StatusView.as_view() name='status'),
    url('payment/bindings/(?P<client_id>[^/]+)/', views.BindingsView.as_view() name='bindings'),
    url('payment/binding/(?P<binding_id>[^/]+)/', views.BindingView.as_view() name='binding'),
    url('payment/history/(?P<client_id>[^/]+)/', views.GetHistoryView.as_view() name='history'),
]
