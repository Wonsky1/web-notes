from django import template
from textwrap import shorten


register = template.Library()


@register.filter(name="truncate_text")
def truncate_text(text, limit=100, ending="..."):
    """
    Truncates text using the textwrap module.

    Args:
        text: The text to be truncated.
        limit: The maximum number of symbols (default: 100).
        ending: The string to append to the truncated text (default: "...").

    Returns:
        The truncated text.
    """

    return shorten(text, width=limit, placeholder=ending)
