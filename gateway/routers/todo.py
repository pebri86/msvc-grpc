import logging, json
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from todo.client import TodoClient

router = APIRouter()

# setup loggers
logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.DEBUG)

# get root logger
logger = logging.getLogger(__name__)


class CreateTodoRequest(BaseModel):
    title: str
    description: str


class UpdateTodoRequest(CreateTodoRequest):
    id: int


@router.post("/v1/create")
async def create_todo(request: Request, todo_request: CreateTodoRequest):
    try:
        user_header = await request.user
        user = json.loads(user_header.message)
        title = todo_request.title
        description = todo_request.description
        client = TodoClient()
        result = await client.create_todo(
            title=title, description=description, user_id=user["ID"]
        )
        return JSONResponse({"success": True, "message": result.message})
    except Exception as err:
        logger.error(err)
        return JSONResponse(
            {"success": False, "message": "Failed to create todo item"}, status_code=400
        )


@router.get("/v1/todos")
async def create_todo(request: Request):
    try:
        user_header = await request.user
        user = json.loads(user_header.message)
        client = TodoClient()
        result = await client.get_todos(user_id=user["ID"])
        return JSONResponse(
            {
                "success": True,
                "message": result.message,
                "data": json.loads(result.data),
            }
        )
    except Exception as err:
        logger.error(err)
        return JSONResponse(
            {"success": False, "message": "Failed to get some todo items"},
            status_code=404,
        )


@router.put("/v1/update")
async def create_todo(request: Request, todo_request: UpdateTodoRequest):
    try:
        user_header = await request.user
        user = json.loads(user_header.message)
        id = todo_request.id
        title = todo_request.title
        description = todo_request.description
        client = TodoClient()
        result = await client.update_todo(id=id, title=title, description=description)
        return JSONResponse({"success": True, "message": result.message})
    except Exception as err:
        logger.error(err)
        return JSONResponse(
            {"success": False, "message": "Failed to update todo item"}, status_code=500
        )


@router.delete("/v1/delete")
async def create_todo(request: Request, todoId: int):
    try:
        user_header = await request.user
        user = json.loads(user_header.message)
        client = TodoClient()
        result = await client.delete_todo(id=todoId)
        return JSONResponse({"success": True, "message": result.message})
    except Exception as err:
        logger.error(err)
        return JSONResponse(
            {"success": False, "message": "Failed to delete todo item"}, status_code=500
        )


@router.get("/v1/todo")
async def create_todo(request: Request, todoId: int):
    try:
        user_header = await request.user
        user = json.loads(user_header.message)
        client = TodoClient()
        result = await client.get_todo(todo_id=todoId, user_id=user["ID"])
        return JSONResponse(
            {
                "success": True,
                "message": result.message,
                "data": json.loads(result.data),
            }
        )
    except Exception as err:
        logger.error(err)
        return JSONResponse(
            {"success": False, "message": "Failed to get todo item"}, status_code=404
        )
