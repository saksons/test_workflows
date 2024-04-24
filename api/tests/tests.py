from fastapi.testclient import TestClient
from api.api import app
from api.log import CustomFormatter
import logging

logger = logging.getLogger("API_tester")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

ch.setFormatter(CustomFormatter())

logger.addHandler(ch)


base_url = "http://0.0.0.0:50901"

client = TestClient(app=app, base_url=base_url)


# API root testig
def test_read_root():
    logger.info("send a request to '/api/v1/'")
    response = client.get("/api/v1/")
    logger.debug(f"response status code: {response.status_code}, response data: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}
    
    
# post method with user data API testing
def test_post_data():
    logger.info("send a request to '/api/v1/some_func_with_data'")
    
    data = {
        "id":0,
        "first_name": "Daniel",
        "last_name": "Safin"
    }
    
    response = client.post("/api/v1/some_func_with_data",
                           headers={"Content-Type": "application/json"},
                           json=data)
    
    logger.debug(f"response status code: {response.status_code}, response data: {response.json()}")
    
    if ("description" in list(data.keys())) and (data["description"]):    
        message = "method edited first name or last name in model and returned it :)"
        expected_status_code = 200
        expected_data  = {
            "message": message,
            "data": {
                "id":0,
                "first_name": data["first_name"]+"_API",
                "last_name": data["last_name"]+"_API",
                "description": data["description"]
            }
        }
    else:
        message = "method didn't edit first name or last name in model because of it hadn't 'description' :("
        expected_status_code = 400
        expected_data = {
            "message": message,
            "data": {}
        }
        
    assert response.status_code == expected_status_code
    assert response.json() == expected_data