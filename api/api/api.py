import fastapi
from fastapi.responses import Response, JSONResponse
from fastapi.requests import Request
from api.test_user_model import TestUserModel
from api.log import CustomFormatter
import logging

logger = logging.getLogger("API")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

ch.setFormatter(CustomFormatter())

logger.addHandler(ch)



app = fastapi.FastAPI()


@app.get("/api/v1/")
async def main(response: Response, request: Request) -> JSONResponse:
    logger.debug(f"from: [client_ip: {request.client[0]}, client_port: {request.client[1]}], to: {request.base_url._url}")
    logger.info(f"this message from root of API :D")
    response.status_code = 200
    return JSONResponse(content={"message": "OK"},
                        status_code=response.status_code)


@app.post("/api/v1/some_func_with_data")
async def some_func_with_data(user: TestUserModel, response: Response, request: Request) -> JSONResponse:
    logger.debug(f"from: [client_ip: {request.client[0]}, client_port: {request.client[1]}], to: {request.base_url._url}")
    match(user.id):
        case -1:
            user.first_name += "_API"
        case 0:
            user.first_name += "_API"
            user.last_name += "_API"
        case 1:
            user.last_name += "_API"
    
    if user.description:
        response.status_code = 200
        message = "method edited first name or last name in model and returned it :)"
        logging.info(message)
        return JSONResponse(content={"message": message, 
                                     "data": {
                                         "id": user.id,
                                         "first_name": user.first_name,
                                         "last_name": user.last_name,
                                         "description": user.description
                                     }},
                            status_code=response.status_code)
        
    response.status_code = 400
    message = "method didn't edit first name or last name in model because of it hadn't 'description' :("
    logging.info(message)
    return JSONResponse(content={"message": message,
                                 "data": {}},
                        status_code=response.status_code)