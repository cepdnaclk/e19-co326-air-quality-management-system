# Ditto Extended API

This API extends the Eclipse Ditto framework for managing digital twins (Things) and access policies in an air quality management system.

## Features
- Create, update, and fetch Things.
- Manage access Policies for Things.
- Acts as an abstraction layer over Eclipse Ditto.

## Prerequisites
- Node.js and npm installed.
- Eclipse Ditto running locally or remotely.

## Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the server:
   ```bash
   npm start
   ```
## Endpoints
* ```POST /thing/:id```: Create a new Thing.
* ```GET /thing/:id```: Retrieve a Thing by ID.
* ```POST /policy/:id```: Create a new Policy.
* ```GET /policy/:id```: Retrieve a Policy by ID.

## How to Use

1. Install Dependencies:

   ```bash
   cd ditto-extended-api
   npm install
   ```
2. Start the API:

   ```bash
   npm start
3. Test Endpoints: Use curl or Postman to test API endpoints:

    * Create a Thing:
      ```bash
      curl -X POST -H "Content-Type: application/json" \
      -d '{"attributes": {"type": "sensor", "location": "City Center"}, "features": {"pm25": {"properties": {"value": 35, "unit": "µg/m³"}}}}' \
  
      http://localhost:3000/thing/air-quality-sensor
    * Get a Thing:
      ```bash
      curl -X GET http://localhost:3000/thing/air-quality-sensor
This API acts as a robust abstraction layer for managing digital twins and policies in your Eclipse Ditto-based air quality management system.