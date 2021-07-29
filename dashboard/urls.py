from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from covid import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',views.indexPage,name='home'),
    url(r'^chatBot/', views.chatBot,name="chatBot"),
    url(r'^prediction/', views.prediction,name="prediction"),
    url(r'^vaccination/', views.vaccination,name="vaccination"),
    url('selectCountry',views.singleCountry,name="single"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
