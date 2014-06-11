from wagtail.wagtailimages.formats import Format, register_image_format, unregister_image_format

unregister_image_format('left')
unregister_image_format('right')
unregister_image_format('fullwidth')

register_image_format(Format('fullwidth', 'Full width', 'richtext-image full-width', 'width-960'))
register_image_format(Format('left', 'Left-aligned', 'richtext-image left', 'width-320'))
register_image_format(Format('right', 'Right-aligned', 'richtext-image right', 'width-320'))

register_image_format(Format('thumb', 'Thumbnail', 'richtext-image thumbnail', 'max-140x140'))