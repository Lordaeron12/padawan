from wagtail.wagtailcore.models import Page
from main.models import MerchantPage

def main_processor(request):
    context = {
        'global_context': {
            'root': Page.objects.all()
        }
    }
    return context
