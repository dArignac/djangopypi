from django import template
from ..models import Package


register = template.Library()


def get_packages():
    """
    Returns the packages ordered by their name.
    """
    return Package.objects.all().order_by('name')

register.assignment_tag(get_packages)
