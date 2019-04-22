from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from case1 import views

router = routers.SimpleRouter()
router.register(r'student',views.StudentVS)


urlpatterns = [
    # Examples:
    # url(r'^$', 'TlxyDRF.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^api/', include(router.urls)),
]
