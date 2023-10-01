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

# Implementation

To access the entire implementation of this challenge, simply visit this [GitHub Repository](https://github.com/JMKobayashi/Tracking-PC)

## Requirements

A virtual environment has been created to facilitate the execution of all parts of this challenge. First and foremost, you will need to download `poetry` if you don't already have it installed. 

To install Poetry, you will need to run `pip install poetry`. Once Poetry is installed, you can create a virtual environment by running the `poetry shell` command. Afterward, use `poetry install` to install all the necessary requirements for this challenge.

## Script

### Script requirements

As previously mentioned, you can use Poetry to create your virtual environment and test all parts of this challenge. However, if you want to install the necessary libraries to run only the script, you will need to install the following Python modules, and of course you will need a Python version instaled:

- requests;
- apscheduler.

To install these modules separately, simply run `pip install <module_name>`.

### Execution

To execute this script you just need to run `python path/to/script.py`

## Track API

### Test

The API is hosted on Google Cloud Platform (GCP), eliminating the need forany installation or manual execution. You can easily test the API by accessing the [documentation created using the FastAPI framework](https://track-challenge-ucu2fzh5qa-uc.a.run.app/docs). However, I recommend using the radio buttons on the left side of this page for a seamless testing experience.

#### Local test

If you wish to test it locally, you can follow the instructions provided in [Implementation - Requirements](#requirements) to create a virtual environment and execute `python src/app.py` to start the Uvicorn server.

Another option is to build and run the Dockerfile located at the project's root directory. To do this, you will need to have Docker installed, and then execute the following commands:

**Build docker image**

```
docker build -t`<your-docker-image-name>` .
```

**Run docker image**

```
docker run -dp`<host-port>`:`<container-port>``<your-docker-image-name>`
```

### How to use this API

This API has two endpoints: `POST /track` and `GET /track/events`. The first endpoint is used to save a dcoument in the database, while the second one is used to retrieve all the events that have been saved in the database.

#### POST /track

To send a request to this endpoint, you have two options: you can click on "Create track information"in the sidebar, or you can use an external tool like Postman or cURL to make a POST request to the following URL `https://track-challenge-ucu2fzh5qa-uc.a.run.app/track`.

When this endpoint is triggered, it initiates the process of saving a new document in MongoDB. For your reference, here's an example of the document:

```json
{
	"_id":"65176b0b7aac873b8c740a7c",
	"event_time":"2023-09-29T21:25:42.747+00:00",
	"request":"POST /track"
}
```

#### GET /track/events

To send a request to this endpoint, you have two options: you can click on "Show track information"in the

sidebar, or you can use an external tool like Postman or cURL to make a GET request to the following URL

`https://track-challenge-ucu2fzh5qa-uc.a.run.app/track/events`.

When this endpoint is triggered, it initiates the process of fetching all the documents stored in MongoDB.

For your reference here's an example of the response

```json
[
   {
      "request": "POST /track",
      "event_time": "2023-09-29T21:25:42.747000",
      "id": "65176b0b7aac873b8c740a7c"
   },
   {
      "request": "POST /track",
      "event_time": "2023-09-29T22:11:47.575000",
      "id": "651775d3d5d22b161e9ff7c4"
   }
]
```
