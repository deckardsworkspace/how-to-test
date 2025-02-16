from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from starlette.status import HTTP_200_OK, HTTP_202_ACCEPTED

from backend.models.database import Database
from backend.views.text.controller import TextController

router = APIRouter()


class WriteTextRequest(BaseModel):
  new_content: str = Field(description='New content for the text file')


class ModifyTextRequest(BaseModel):
  operation: str = Field(
    description='What operation to perform on the text saved to database'
  )


@router.get('/read')
def read_text() -> JSONResponse:
  content = Database.read()

  return JSONResponse(content={'content': content}, status_code=HTTP_200_OK)


@router.post('/write')
def write_text(request: WriteTextRequest) -> JSONResponse:
  Database.write(request.new_content)
  new_content = Database.read()

  return JSONResponse(
    content={
      'message': 'Text file updated successfully',
      'new_content': new_content,
    },
    status_code=HTTP_200_OK,
  )


@router.post('/modify')
def modify_text(request: ModifyTextRequest) -> JSONResponse:
  content = Database.read()

  result = TextController.modify_text(operation=request.operation, text=content)
  Database.write(result)

  new_content = Database.read()

  return JSONResponse(
    content={
      'message': 'Operation successful',
      'operation': request.operation,
      'new_content': new_content,
    },
    status_code=HTTP_202_ACCEPTED,
  )
