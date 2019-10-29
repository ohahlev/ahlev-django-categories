from django.db import models
from django.template.defaultfilters import truncatechars
from fontawesome_5.fields import IconField
from django.utils.html import format_html
from django.core.exceptions import ValidationError


def validate_icon_empty(value):
    """
    {'name': '', 'style_prefix': '', 'kwargs': {'prefix': 'fa'}}
    """
    if value.name == '':
        raise ValidationError('icon is required')


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
        
    name = models.CharField(max_length=32, unique=True, null=False)
    icon = IconField(unique=True, validators=[validate_icon_empty])
    detail = models.TextField(max_length=1025)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    def short_detail(self):
        return truncatechars(self.detail, 30)
    
    short_detail.admin_order_field = 'detail'
    short_detail.short_description = 'detail'
    
    def get_icon(self):
        if self.icon:
            return format_html("<span><i class='%s %s-lg %s-%s'></i></span>" 
                % (self.icon.style_prefix, self.icon.kwargs["prefix"], 
                self.icon.kwargs["prefix"], self.icon.name))

    get_icon.short_description = 'icon'