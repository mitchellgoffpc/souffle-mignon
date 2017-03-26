from datetime import datetime

from django import template

register = template.Library()


@register.filter
def urlify(text):
    return ' '.join(map(helper, text.split()))

def helper(word):
    if word[0] == '@':
        return '<a href="https://twitter.com/{}" target="_blank">{}</a>'.format(word[1:], word)
    elif word[:4] == 'http':
        return '<a href="{}" target="_blank">{}</a>'.format(word, word)
    else:
        return word


@register.filter
def to_date(text):
    return datetime.strptime(text, '%a %b %d %H:%M:%S +0000 %Y')
