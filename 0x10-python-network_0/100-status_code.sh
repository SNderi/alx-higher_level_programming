#!/bin/bash
# Sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -sw "%{response_code}" "$1" -o /dev/null
