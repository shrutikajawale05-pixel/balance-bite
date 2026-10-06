from django import template
from django.apps import apps
from django.db.models import Sum

register = template.Library()

@register.simple_tag
def get_count(model_name):
    try:
        app_label, model = model_name.split('.')
        Model = apps.get_model(app_label, model)
        return Model.objects.count()
    except:
        return 0

@register.simple_tag
def get_revenue():
    try:
        Order = apps.get_model('parlour', 'Order')
        total = Order.objects.aggregate(Sum('total_amount'))['total_amount__sum']
        # jar field name vegla asel tar 'total_price' karun bagh
        if not total:
            total = Order.objects.aggregate(Sum('total_price'))['total_price__sum']
        return total or 0
    except:
        return 0