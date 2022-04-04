from django.urls import path
from .views import demo_plot_view, plot_from_models, pie_chart_from_models


urlpatterns = [
    path('', demo_plot_view),
    path('pie_chart/', pie_chart_from_models),
    path('models/', plot_from_models),
]
