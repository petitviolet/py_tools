# -*- encoding:utf-8 -*-
from __future__ import print_function
import requests


def fetch_html_with_encoding(url):
    ''' Return html and encoding of url
    Args:
        url: url you want to fetch html
    Return:
        html, encoding if fetch html succeeded, else False, False
    '''
    try:
        result = requests.get(url)
        if result.ok:
            return result.content, result.encoding
        else:
            print('error ...', result, url)
    except Exception as e:
        print(e)
    return False, False

