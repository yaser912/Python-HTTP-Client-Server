# HTTP Library

def makeGetRequest(url, header=None, **kwargs):
    requestedString = ("GET " + url + " HTTP/1.0\r\n")

    if header is not None:
        for key, value in header.items():
            requestedString += ("{0}: {1}".format(key, value) + "\r\n")

    for key, value in kwargs.items():
        requestedString += ("{0}: {1}".format(key, value) + "\r\n")
    requestedString += "\r\n"
    return requestedString


def makePostRequest(url, header=None, data=None, json=None, **kwargs):
    requestedString = ("POST " + url + " HTTP/1.0\r\n")

    if header is not None:
        for key, value in header.items():
            requestedString += ("{0}: {1}".format(key, value) + "\r\n")

    if kwargs is not None:
        for key, value in kwargs.items():
            requestedString += ("{0}: {1}".format(key, value) + "\r\n")

    # additional carriage return/line feed before Entity Body
    requestedString += ("\r\n")

    # Entity body
    if data is not None:
        for key, value in data.items():
            requestedString += ("{0}: {1}".format(key, value) + "\r\n")

    if json is not None:
        requestedString += json

    requestedString += "\r\n"
    return requestedString


def addQuery(url, params, **kwargs):
    url += "?"
    count = 0
    if kwargs is not params:
        for key, value in params.items():
            if count != 0:
                url += "&"  # if count is not 0, url+= &
            url += ("{0}={1}".format(key, value))
            count += 1

    return url


def getStatusLine(response):

    statusLine = response.split('\r\n', 1)
    statusLine = statusLine[0]
    return statusLine


# split between /r/n and /r/n/r/n
def getRequestHeader(response):
    statusLine, header = response.split('\r\n', 1)
    actualHeader, actualBody = header.split('\r\n\r\n', 1)

    return actualHeader


# make a method that retreives headers from a GET response.
def getRequestBody(response):

    _, body = response.split('\r\n\r\n', 1)

    return body

