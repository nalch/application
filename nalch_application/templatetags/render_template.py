from django import template
from django.template import (
    Context,
    Template
)


register = template.Library()


@register.simple_tag
def render_template(text, **kwargs):
    texttemplate = Template(text)
    context = Context(kwargs)
    return texttemplate.render(context)
