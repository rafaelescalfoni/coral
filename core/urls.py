from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('project/<int:id>', views.project, name='project'),
    path('graph_specialist/<int:proj_id>', views.graph_specialist, name='graph_specialist'),
    path('graph_reputation/<int:proj_id>', views.graph_reputation, name='graph_reputation'),

    # Rota ghost
    path('graph_reputation_filter/<int:proj_id>', views.graph_reputation_filter, name='graph_reputation_filter'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]