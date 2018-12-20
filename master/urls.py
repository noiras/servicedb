from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'master'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<id>',views.view_detail_dashboard, name='detail_dashboard'),
    path('viewtable/', views.viewtable, name='viewtable'),
    path('delete/<id>/', views.delete_table, name='deleteTable'),
    path('viewsdetailstable/<id>/', views.viewsdetailstable,name='detail_table' ),
    path('updatevalue/', views.updatevalue, name='updatevalue'),
    path('deletevalue/', views.deletevalue, name='deletevalue'),
    path('tablejson/', views.tablejson, name='tablejson'),
    path('tablejson/<id>', views.valuejson, name='detail_tablejson'),
    path('updatecolumn/', views.updatecolumn, name='updatecolumn'),
    path('deletecolumn/', views.deletecolumn,name='detailcolumn'),
    path('viewsaddcolumn/<id>', views.viewsaddcolumn, name='viewsaddcolumn'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)