import requests

def requests_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + 'query_char'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, try again! ')

#Password API #226

def pwned_api_check(password): #check password if it exists in API res
    pass
requests_api_data('123')