#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib.error import HTTPError
    import sys

    try:
        with urlopen(sys.argv[1]) as response:
            res = response.read()
            res_decoded = res.decode('utf8', "replace")
            print(res_decoded)
    except HTTPError as err:
        print("Error code: {}".format(err.code))
