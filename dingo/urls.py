from django.contrib import admin
from django.urls import path, include
from dingo.views import logout_view  
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from dingo.api import router

urlpatterns = [
   path('admin/', admin.site.urls),
   path('maths/', include("maths.urls")),
   path('greetings/', include('greetings.urls')), 
   path('sessions/', include("sessions.urls")),
   path('posts/', include("posts.urls")),
   path('',  include("home.urls") ),
   path('about/',  include("about.urls") ),
   path('contact/',  include("contact.urls") ),
   
   path('accounts/logout/', logout_view, name='logout'),
   path('accounts/', include('django.contrib.auth.urls')),
   path('admin/', admin.site.urls),
   path('about/', TemplateView.as_view(template_name="about/about.html")),

   path('grappelli/', include('grappelli.urls')),
   path('admin/', admin.site.urls),

   path('api/v1/', include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)