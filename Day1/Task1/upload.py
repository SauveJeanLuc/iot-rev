import requests

data = {
    'device': 'roup',
    'distance': '3.5 cm'
}
try:
    res = requests.post('http://insecure.benax.rw/iot/', json=data)
    res.raise_for_status()
    print('Success!')
    if res is not None:
        print(res.json())
except requests.exceptions.HTTPError as err:
    print(f"Error {res.status_code}: {res.json()}, for {res.request}: {res.url}")
except Exception as err:
    print(f"Error {err}")  