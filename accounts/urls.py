from django.conf.urls import url
#introduced a login/logout view so we don't have to take care of it in views.  
#its in contrib.auth.  we are renaming it as auth_views for clarification
from django.contrib.auth import views as auth_views
from . import views

#so when I want to use url templates in base.html for example i can refer to it
app_name = 'accounts'


urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # no template_name for logout view because user will go back to the home page
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$', views.SignUp.as_view(), name='signup'),


]
