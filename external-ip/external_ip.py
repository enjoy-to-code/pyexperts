import urllib.request
import re

print("Use dyndns, in order to get IP Address")

url = "http://checkip.dyndns.org"

with urllib.request.urlopen("http://checkip.dyndns.org") as url:
    request = url.read()

external_ip = re.findall(r"(?:\d{1,3}\.)+(?:\d{1,3})", str(request))
print("your IP Address is: ",  external_ip)


