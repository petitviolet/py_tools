# -*- encoding:utf-8 -*-
'''

'''

import requests


def fetch_html(url):
    ''' urlを与えるとhtmlとencodingを返す
    '''
    try:
        result = requests.get(url)
    except Exception as e:
        print(e)
        return False, False
    if result.ok:
        return result.content, result.encoding
    else:
        print('error ...', result, url)
        return False, False

