# This README.md file was created by ChatGPT 3.5 & have some edited by me :D

# Test API for testing github actions (workflows)

This API needed just for testing github actions.

## Endpoints

### 1. Root Endpoint

- **URL:** `/api/v1/`
- **Method:** `GET`
- **Description:** Returns a simple message indicating that the API is operational.
- **Request Parameters:** None
- **Response:** JSON with a success message.

### 2. Endpoint with Data Processing

- **URL:** `/api/v1/some_func_with_data`
- **Method:** `POST`
- **Description:** Processes data and modifies user details based on certain conditions.
- **Request Parameters:**
  - `user`: JSON object containing user details.
    - `id`: User ID (integer | string).
    - `first_name`: First name of the user (string).
    - `last_name`: Last name of the user (string).
    - `description`: Description of the user (string).
- **Response:** JSON with a message indicating success or failure, along with modified user details (if applicable).

## Usage

1. Ensure you have Python installed on your machine.
2. Install the poetry on your machine using the following [link](https://python-poetry.org/docs/)
3. Install the required dependencies using the following commands:

```bash
cd ./api
poetry install
```

4. Run the main file using the following command:
```bash
poetry run python main.py
```

5. Once the server is running, you can access the endpoints using appropriate HTTP requests.

## Example

### Request

```http
POST /api/v1/some_func_with_data HTTP/1.1
Host: localhost:8000
Content-Type: application/json

{
"user": {
 "id": 1,
 "first_name": "John",
 "last_name": "Doe",
 "description": "Example description."
}
}
```

### Response
```json
{
  "message": "method edited first name or last name in model and returned it :)",
  "data": {
    "id": 1,
    "first_name": "John_API",
    "last_name": "Doe_API",
    "description": "Example description."
  }
}
```

## Configuration

```json
    {
        "python":"3.11.6",
        "poetry":"1.8.2",
        "packages":{
            "fastapi": "^0.110.2",
            "uvicorn": {
                "extras": ["standart"],
                "version": "^0.29.0"
                },
            "pytest": {
                "version": "^8.1.1",
                "dependence": {
                    "httpx": "^0.27.0"
                }
            }
        }
    }
```