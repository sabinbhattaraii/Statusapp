from django.urls import path

from .views import StatusMessageCreateView,StatusMessageDeleteView

app_name = "statusapp"

urlpatterns = [
    #/statusapp/create/
    path('create/',StatusMessageCreateView.as_view(),name='create'),
    path('delete/<int:pk>/',StatusMessageDeleteView.as_view(),name='delete')
]