import os
import base64
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
correctRequest = " 200 OK\n"
badRequest = " 400 Bad Request\n"
serverDetails = "\nServer: Simple HTTP Server"
connectionType = "\nConnection: closed"
credentials = "yaser:aleem"


def process_request(data):
    access = False
    data = data.decode("utf-8")
    for item in data.split("\n"):  # security
        if "Authorization: " in item:
            credsHeader = item
            credsParts = credsHeader.split()  # convert authorization header string to list
            inputCredentials = base64.b64decode(credsParts[2])
            inputCredentials = inputCredentials.decode("utf-8")
            if inputCredentials == credentials:
                access = True

    files = [f for f in os.listdir()]
    response = ""
    if len(data) != 0:
        requestLine = data.partition('\r\n')[0]
        requestParts = requestLine.split()  # requestParts is the array that holds the request line
        method = requestParts[0]
        path = requestParts[1]
        version = requestParts[2]
        if access:
            if method == 'GET':
                response = version
                if path[1:] not in files and path != '/' and '/' not in path[1:]:
                    if "?" in path[1:]:  # handle query params, return the arguments in the body.
                        response += correctRequest
                        response = appendHeaders(response)
                        response = handleQuery(response, path)
                        return response
                    response += badRequest
                    print(response)
                else:
                    response += correctRequest
                    response = appendHeaders(response)
                    response = appendBody(response, path)

            if method == 'POST':
                response = version
                response += correctRequest
                response = appendHeaders(response)
                appendToFile(data, path[1:])

            if method == 'HEAD':
                response = version
                response += correctRequest
                response = handleHeaders(response)

        else:
            response += version
            response += badRequest
            print(response, " Due to security reasons.")

    return response


def appendHeaders(response):
    response += f'{"Date: "}{dt_string}'
    response += serverDetails
    response += connectionType

    return response


def handleQuery(response, path):
    response += "\r\n\r\n"
    # return query param args in body
    response += "\nQuery arguments:\n"
    _, args = path.split('?', 1)
    args = args.replace("=", " : ")
    if "&" in args:
        args = args.replace("&", "\n")
    response += args
    return response


def handleHeaders(response):
    # if client requesting headers of the server:
    response += "Headers requested:\n"
    response += f'{"Date: "}{dt_string}'
    response += serverDetails
    response += connectionType

    return response


def appendBody(response, path):
    if '/' in path:
        path = path.split('/')
        response += "\r\n"
        directory = os.getcwd()
        directory += '\\'
        directory += path[1]

    else:
        response += "\r\n"
        directory = os.getcwd()
        directory += path

    response += "\r\n"  # empty line before contents of body
    files = [f for f in os.listdir(directory)]
    for f in files:
        if f in path:
            directory += "\\"
            directory += f
            file = open(directory)
            response += file.read()
            return response
        response += "\n"
        response += f

    return response


def appendToFile(data, pathOfFile):
    exists = False
    _, body = data.split('\r\n\r\n', 1)  # body  now contains details we must add to file.

    if ".txt" not in pathOfFile:
        pathOfFile += ".txt"
    directory = os.getcwd()
    directory += '\\'
    directory += pathOfFile
    files = [f for f in os.listdir()]
    for f in files:
        if f in pathOfFile:  # if file is in directory then overwrite to it
            exists = True
            file = open(directory, 'w')
            file.write(body)
            return

    if not exists:  # file does not exist, so we must create and write to it
        file = open(pathOfFile, "x")
        file.write(body)

    return
