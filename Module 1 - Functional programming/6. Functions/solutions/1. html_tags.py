def html_wrapper(tag, text):
    result = f'<{tag}>{text}</{tag}>'
    return result

paragraph = html_wrapper(tag='p', text='This is a paragraph')
print(paragraph)

div = html_wrapper(tag='div', text='This is a div')
print(div)