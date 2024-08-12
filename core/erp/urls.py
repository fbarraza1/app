from django.urls import path

from core.erp.views.dashboard.views import *

from core.erp.views.tests.views import TestView

from core.erp.views.tiposprod.views import *

from core.erp.views.poste.views import *

app_name = 'erp'

urlpatterns = [   
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # test
    path('test/', TestView.as_view(), name='test'),
    # sale
    
    path('tipoprod/list/', TipoProdListView.as_view(), name='tipoprod_list'),
    path('tipoprod/add/', TipoProdCreateView.as_view(), name='tipoprod_create'),
    path('tipoprod/update/<int:pk>/', TipoProdUpdateView.as_view(), name='tipoprod_update'),
    path('tipoprod/delete/<int:pk>/', TipoProdDeleteView.as_view(), name='tipoprod_delete'),

    #poste
    path('poste/list/', PosteListView.as_view(), name='poste_list'),
    path('poste/add/', PosteCreateView.as_view(), name='poste_create'),
    path('poste/update/<str:pk>/', PosteUpdateView.as_view(), name='poste_update'),
    path('poste/delete/<str:pk>/', PosteDeleteView.as_view(), name='poste_delete'),
    

]
