from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', views.dashboard),
    path('dashboard/<id>',views.editdashboard),
    path('viewtable/', views.viewtable),
    path('delete/<id>/', views.delete),
    path('viewsdetails/<id>/', views.viewsdetails),
    path('updatevalue/', views.updatevalue),
    path('deletevalue/', views.deletevalue),
    path('tablejson/', views.tablejson),
    path('tablejson/<id>', views.valuejson),
    path('updatecolumn/', views.updatecolumn),
    path('deletecolumn/', views.deletecolumn),
    path('viewsaddcolumn/<id>', views.viewsaddcolumn),

    # tables/
    # tables/id
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)