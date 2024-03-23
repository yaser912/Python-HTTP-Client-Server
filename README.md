# Python-HTTP-Client-Server
Simple implementation of an HTTP client and server in Python


Client:

This assignment involves implementing a simple HTTP client application similar to cURL. The tasks include:

Setting up the development and testing environment.
Studying the HTTP network protocol specifications, focusing on HTTP version 1.0.
Building a custom HTTP client library using TCP sockets to support GET and POST operations, query parameters, request headers, and request body.
Providing detailed usage instructions for httpc, including examples for GET and POST requests with various options.
Ensuring compatibility with major operating systems and recommending the use of version control (Git) and network tools (Wireshark).
The assignment encourages experimentation with telnet for understanding HTTP protocol specifications. 

Server:
This assignment focuses on implementing a simple HTTP server application to create a remote file manager using the HTTP protocol. The tasks include:

Studying and reviewing the HTTP network protocol specifications, emphasizing server-side features and considering HTTP version 1.0.
Developing an HTTP server library using minimal socket APIs provided by the chosen programming language, implementing a subset of HTTP specifications.
Building a file server application on top of the HTTP library, with functionalities such as retrieving a list of files, accessing file contents, and creating or overwriting files through GET and POST requests.
Addressing security concerns by preventing access to files outside the server's working directory.
Enhancing error handling by translating exceptions to appropriate status codes and human-readable messages.
Providing usage instructions for the file server application, including options for specifying port number and directory.
The implementation must use only bare-minimum socket APIs without leveraging any libraries that abstract socket programming. Additionally, the file server application should support multiple file formats for responses and provide error handling mechanisms. The usage instructions include options for verbose mode, specifying port number, and directory for reading/writing files.


