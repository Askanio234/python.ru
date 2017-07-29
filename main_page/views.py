from django.views.generic import TemplateView
from banners.models import Banner
from cards_api.models import Card


class MainPage(TemplateView):
    template_name = 'main_page/main_page.html'

    def get_context_data(self, **kwargs):
        ctx = super(MainPage, self).get_context_data(**kwargs)
        ctx['cards'] = Card.objects.all()
        ctx['banners'] = {b['slug']: b['image'] for b in Banner.objects.values()}
        return ctx
