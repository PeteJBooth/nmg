from django import template
from bs4 import BeautifulSoup

# ----------------------------------------------------------------------------

register = template.Library()


@register.filter
def highlight_first_paragraph(content, class_name):

    """This tag adds a class to the first paragraph."""
    soup = BeautifulSoup(content)
    paragraph = soup.find('p')
    if paragraph:
        paragraph['class'] = class_name
    return soup.renderContents()