"""
URL configuration for first project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path, re_path

urlpatterns = [
    path('', include("home.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('favs', include("favs.urls")),
    path('menu/', include("menu.urls")),
    path('pics/', include("pics.urls")),
    path('forums/', include("forums.urls")),
    path('chat/', include("chat.urls")),
    path('admin/', admin.site.urls),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
]

# Switch to social login if it is configured
try:
    from . import github_settings
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0,
        path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login))
    )
    print('Using', social_login, 'as the login template')
except:
    print('Using registration/login.html as login template, SHIIIIIT')

