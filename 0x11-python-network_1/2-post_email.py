#!/usr/bin/python3
""" Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response.
"""


if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    import sys

    url = sys.argv[1]
    val = {'email': sys.argv[2]}
    data = urlencode(val)
    data = data.encode('ascii')
    req = Request(url, data)
    with urlopen(req) as response:
        body = response.read()
        body_decoded = body.decode('utf-8', "replace")
        print(body_decoded)
