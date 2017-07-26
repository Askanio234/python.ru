from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from articles.views import ArticleView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/cards/', include('cards_api.urls')),
    url(r'^articles/(?P<pk>\d+)/', ArticleView.as_view()),
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
