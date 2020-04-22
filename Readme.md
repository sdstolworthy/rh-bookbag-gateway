# Project Bookbag API Gateway

This gateway serves as an intermediary between the Project Bookbag Frontend and the Openshift cluster and other resources from which the frontend pulls data.

This gateway proxies requests to the Openshift cluster, serializes responses from the cluster, and returns them to the client.

Currently, the API authenticates with Openshift using a service token. 
The service token is loaded in an environment variable (see `.env.example` for an example of how this should look).

The API makes requests to the Openshift API through cluster's REST API.

## Up and Running
Starting the server is simple. First, install all necessary dependencies with `pip install -r requirements.txt` and then `pipenv install`.

Create a copy of `.env.example` name `.env`. Copy over the required values.

You may also need to make the start script executable `chmod +x ./start.sh`

With the requirements installed and the `.env` file configured correctly, we are ready to start the server. Start the development server with `./start.sh`.

By default, the server will listen for requests on port `5000`.

With the server running, you can make a test request curl: `curl --location --request GET 'localhost:5000/api/resources'`

## Project structure

The project is organized into subsections. The primary application is found in `bookbag/`.
In `bookbag/` each of the subsections has its own folder.

### Schemas
`bookbag/schemas` contains the the model definitions. Each schema is defined in its own eponymous file.

### Serializers
`bookbag/serializers` contains the serializer classes. The serializers handle converting objects from an external api's specification to a schema native to this application. 

### Services
`bookbag/services` contains the implementation details for fetching data from an external resource and performing business logic on that data. They also call serializers to convert data where necessary.

### Transport
`bookbag/transport` encapsulates Flask specific transport logic. Incoming HTTP requests are handled in `transport/`.

### Flask Config files
At the root of `bookbag/`, several config files exist to bootstrap the flask application.
`app.py` handles starting the flask application.
`config.py` sets global config variables for the app.
`extensionsl.py` contains several helpers that are useful throughout the application, or that should be applied to the main flask instance to extend its functionality (e.g. the CORS module).
`settings.py` contains Flask specific settings variables.

