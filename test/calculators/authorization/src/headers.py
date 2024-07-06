
def headers():
    return {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=utf-8',
        'Origin': 'https://club.gteh.pro',
        'Referer': 'https://club.gteh.pro/account',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, как Gecko) Chrome/126.0.0.0 Safari/537.36'
    }


def headers_token(token):
    header = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': '_ym_uid=1719861385611584143; _ym_d=1719861385; _ym_isad=2; _ym_visorc=w; GTEH=MTcxOTg2MTQ5N3xWS1BxY3dzNC1zSVlKczVSODhja1JUVHBWWE81eHZKbTQyYm9BV3RPLU5uaTZ5WWQzUW1fWnAxUXRMRmtva2RnN3NxQzdXcXRJWVBSNjBQTnhhaFc0bzhhMDUycEw5Q2xpMjNRQ1lqQlFOYlluc2xaYVRneXYxRk43dGtMfO6GNxPvfoQL9qvyO9tbYVH1fEUXLnKoX2D9ae0yW0J9',
        'Host': 'club.gteh.pro',
        'Referer': 'https://club.gteh.pro/account',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, как Gecko) Chrome/126.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'token': f'{token}'
    }
    return header
