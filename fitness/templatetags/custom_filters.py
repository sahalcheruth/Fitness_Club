from django import template

# Register the template library to use custom filters in templates
register = template.Library()

# =====================================
#  repeat filter
# =====================================

@register.filter
def repeat(value):
    try:
        return range(int(value))
    except (ValueError, TypeError):
        return []  # Safe fallback if invalid input


# =====================================
#  add_class filter
# =====================================

# Adds custom CSS classes to form fields
@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})
