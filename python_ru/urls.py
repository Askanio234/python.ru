from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from main_page.views import MainPage


urlpatterns = [
    url(r'^$', MainPage.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^api/cards/', include('cards_api.urls')),
    url(r'^articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
