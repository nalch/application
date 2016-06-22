from django import template
from django.template import (
    Context,
    Template
)


register = template.Library()


@register.simple_tag
def render_template(text, **kwargs):
    """
    render a template string with a context derived from the keyword arguments
    :param text: the string to be rendered
    :type text: str
    :param kwargs: the keywordarguments, that are keys and values of the generated context
    :type kwargs: dict
    :return: the rendered template
    :rtype str
    """
    texttemplate = Template(text)
    context = Context(kwargs)
    return texttemplate.render(context)
