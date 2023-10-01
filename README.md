# Description

Joe has some sketchy roommates, and he is suspicious that they might be using his PC when he isnot at home. So he wants to keep track of when his home PC is turned on by running a script in the background to poll his webserver once per minute.

1. Write Joe's background script that he can run on his home PC. This script can be written in any language, and you can assume that Joe can figure out how to automatically run it when the machine boots. It should make requests to the web server to tell when the computer is on.

   - Once the script starts, it should run forever
   - It should make a request to the server once per minute
2. Create the back-end:

   - A web server (this can run on a cloud server, or your local PC if you can host it behind your router)
   - A REST endpoint that logs a request from the home PC. This can use any framework inany language you prefer (PHP, Python, node.js, etc.)
   - Some kind of storage (any database, your choice) to keep track of the request history
   - A web page that displays the history of requests. This can just be a plain text list of requests and their timestamps.

# Documentation
To access the full documentation click in [this link]()