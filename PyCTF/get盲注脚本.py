import requests
url1 = "192.168.10.120/DVWA/vulnerabilities/sqli_blind/?id="
url2 = "&Submit=Submit"
def get_dataname():
    for i in range(32,128):
        pyload = "1'' and '' = '' ; "
        
