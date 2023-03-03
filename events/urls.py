from django.urls import path
from .views import *
# from .views import *

urlpatterns = [
    path('', homePage, name="Home_Page"),
    path('home/', homePage1, name="Home_Page1"),
    path('listStatic/', listEventsStatic, name="Events_listS"),
    path('listEvent/', listEvents, name="Events_list"),
    path('detail/<int:id>', detailEvent, name="Events_detail"),
    path('listV/', EventListView.as_view(), name="Events_listV"),
    path('detailV/<int:pk>', EventDetails.as_view(), name="Events_detailV"),
    path('add/', addEvent, name="Events_add"),
    path('addEv/', EventCreateView.as_view(), name="Events_addM"),
    path('editEv/<int:pk>', EventUpdateView.as_view(), name="Events_editM"),
    path('deleteEv/<int:pk>', delete_event, name="Event_delete"),
    path('participateEv/<int:pk>', participate, name="Event_participate")
]


