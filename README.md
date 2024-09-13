# Picture Management API

This project provides a **Flask-based API** for managing a collection of pictures stored in a JSON file. The API supports operations for creating, retrieving, updating, and deleting pictures, and comes with test cases for validating each endpoint. The application uses `Flask` and stores the picture metadata, such as event details and picture URLs, in a `pictures.json` file.

## Features

- **Health Check**: Simple endpoint to verify the health of the API.
- **Picture Management**:
  - **Create** a new picture.
  - **Retrieve** all pictures or a specific picture by ID.
  - **Update** an existing picture by ID.
  - **Delete** a picture by ID.
- **Data Storage**: All picture data is stored in the `pictures.json` file and can be updated via the API.
  
## Data Structure

The picture data is stored as JSON and includes the following fields:

- `id`: Unique identifier for the picture.
- `pic_url`: URL of the picture.
- `event_country`: Country where the event occurred.
- `event_state`: State where the event occurred.
- `event_city`: City where the event occurred.
- `event_date`: Date of the event in `MM/DD/YYYY` format.

### Example JSON Entry:

```json
{
    "id": 2,
    "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000",
    "event_country": "United States",
    "event_state": "*Florida",
    "event_city": "Naples",
    "event_date": "11/2/2022"
}
```

## API Endpoints

### Health Check

**GET /health**

Checks the health of the application.

#### Response:
```json
{
  "status": "OK"
}
```

## Count Pictures

**GET /count**

Returns the total number of pictures.

#### Response:
```json
{
  "length": 10
}
```
## Get All Pictures

**GET /picture**

Retrieves the full list of pictures.

#### Response:
```json
[
  {
    "id": 2,
    "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000",
    "event_country": "United States",
    "event_state": "*Florida",
    "event_city": "Naples",
    "event_date": "11/2/2022"
  },
  ...
]
```

## Get Picture by ID

**GET /picture/<int:id>**

Retrieves a specific picture by its ID.

#### Response:
```json
{
  "id": 2,
  "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000",
  "event_country": "United States",
  "event_state": "*Florida",
  "event_city": "Naples",
  "event_date": "11/2/2022"
}
```


## Create a Picture

**POST /picture**

Adds a new picture to the collection.

### Request Body:
```json
{
  "id": 11,
  "pic_url": "http://dummyimage.com/123x100.png/5fa2dd/ffffff",
  "event_country": "United States",
  "event_state": "California",
  "event_city": "Fremont",
  "event_date": "11/2/2030"
}
```

### Response: 201 Created
```json
{
  "id": 11,
  "pic_url": "http://dummyimage.com/123x100.png/5fa2dd/ffffff",
  "event_country": "United States",
  "event_state": "California",
  "event_city": "Fremont",
  "event_date": "11/2/2030"
}
```
### If the picture with the same ID already exists:
### Response: 302 Found

```json
{
  "Message": "picture with id 11 already present"
}
```



## Update a Picture

**PUT /picture/<int:id>**

Updates an existing picture by its ID.

### Request Body:
```json
{
  "id": 2,
  "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000",
  "event_country": "United States",
  "event_state": "*Florida",
  "event_city": "Naples",
  "event_date": "11/2/2022"
}
```

### Response: 200 OK
```json
{
  "id": 2,
  "pic_url": "http://dummyimage.com/230x100.png/dddddd/000000",
  "event_country": "United States",
  "event_state": "*Florida",
  "event_city": "Naples",
  "event_date": "11/2/2022"
}
```

## Delete a Picture

**DELETE /picture/<int:id>**

Deletes a picture by its ID.

### Response: `204 No Content`

### If the picture doesn't exist:

**Response: `404 Not Found`**
```json
{
  "message": "Picture not found"
}
```

## Running Tests

You can run the tests using `pytest`. The test suite ensures that the endpoints are working as expected and the data is correctly handled.

```bash
pytest
```
