from wagtail.wagtailcore import hooks
from django.utils.html import format_html, format_html_join
from django.conf import settings

def editor_js():
  return format_html(
    """
    <script>
      registerHalloPlugin('hallohtml');
    </script>
    """
  )
hooks.register('insert_editor_js', editor_js)

def editor_css():
  return format_html('<link rel="stylesheet" href="' \
  + settings.STATIC_URL \
  + 'website/editor.css">')
hooks.register('insert_editor_css', editor_css)