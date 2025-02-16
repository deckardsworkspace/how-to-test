from fastapi.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST


class TextController:
  @staticmethod
  def make_uppercase(text: str) -> str:
    return text.upper()

  @staticmethod
  def make_sentence_case(text: str) -> str:
    return text.capitalize()

  @staticmethod
  def make_lowercase(text: str) -> str:
    return text.lower()

  @classmethod
  def modify_text(cls, operation: str, text: str) -> str:
    if operation == 'lowercase':
      return cls.make_lowercase(text)
    elif operation == 'uppercase':
      return cls.make_uppercase(text)
    elif operation == 'sentence_case':
      return cls.make_sentence_case(text)

    raise HTTPException(
      status_code=HTTP_400_BAD_REQUEST, detail=f'Invalid operation "{operation}"'
    )
