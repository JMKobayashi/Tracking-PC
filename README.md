# Track PC Turn on

### Objectives

1. Write Joe's background script that he can run on his home PC. This script can be written in any language, and you can assume that Joe can figure out how to automatically run it when the machine boots. It should make requests to the web server to tell when the computer is on.
   1. Once the script starts, it should run forever
   2. It should make a request to the server once per minute
2. Create the back-end
   1. A web server (this can run on a cloud server, or your local PC if you can host it behind your router)
   2. A REST endpoint that logs a request from the home PC. This can use any framework in any language you prefer (PHP, Python, node.js, etc.)
   3. Some kind of storage (any database, your choice) to keep track of the request history
   4. A web page that displays the history of requests. This can just be a plain text list of requests and their timestamps.
