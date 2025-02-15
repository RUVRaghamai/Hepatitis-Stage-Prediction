from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm



urlpatterns = [
    path("", views.home,name="home"),



    path("registration/",views.CustomerRegistrationView.as_view(), name="customerregistration"),
    path("accounts/login/", views.CustomLoginView.as_view(), name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('predict/', views.predict_stage, name='predict_stage'),
    path('result/', views.result, name='result'),  # URL pattern for result

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
