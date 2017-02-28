from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^notes/$',views.showNotes,name="notes"),
    url(r'^note/new/$',views.addNotes,name = 'addNotes'),
    url(r'^mail/$',views.Email,name = 'Email'),
    url(r'^note/search/$',views.search,name = 'searchNotes'),
    url(r'^note/upload/$',views.uploads,name= 'uploadsucess'),
    url(r'^(?P<id>\d+)/delete/$',views.notes_delete,name='delete_notes'),
    url(r'^note/(?P<pk>\d+)/$',views.showNotes,name = 'Notes'),
]