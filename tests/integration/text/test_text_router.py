from secrets import token_urlsafe
from typing import Dict, Optional

import pytest
from requests import request
from requests.exceptions import HTTPError
from starlette.status import HTTP_400_BAD_REQUEST


def make_request(
  endpoint: str, method: str, body: Optional[Dict[str, str]] = None
) -> Dict[str, str]:
  path = f'http://localhost:12345/text/{endpoint}'

  response = request(method=method, url=path, json=body)

  # If the response code isn't HTTP 2xx, raise an HTTPError
  response.raise_for_status()

  return response.json()


class TestTextRouter:
  def test_read_text(self) -> None:
    response = make_request(
      endpoint='read',
      method='GET',
    )

    assert response is not None
    print(response)

  def test_write_text(self) -> None:
    random_text = token_urlsafe(16)

    response = make_request(
      endpoint='write',
      method='POST',
      body={'new_content': random_text},
    )

    assert 'message' in response
    assert response['message'] == 'Text file updated successfully'

    assert 'new_content' in response
    assert response['new_content'] == random_text

    print(response)

  def test_modify_text(self) -> None:
    sample_sentence = 'the quick brown fox jumped over the lazy dog'

    # Write to database
    response = make_request(
      endpoint='write',
      method='POST',
      body={'new_content': sample_sentence},
    )

    assert response['new_content'] == sample_sentence

    # Modify text in database
    response = make_request(
      endpoint='modify', method='POST', body={'operation': 'sentence_case'}
    )

    assert response['new_content'] == 'The quick brown fox jumped over the lazy dog'

  def test_modify_text_should_raise(self) -> None:
    invalid_operation_name = 'what the sigma'

    with pytest.raises(HTTPError) as e:
      make_request(
        endpoint='modify',
        method='POST',
        body={'operation': invalid_operation_name},
      )

    assert e.value.response.status_code == HTTP_400_BAD_REQUEST

    # Raising an HTTPException in FastAPI returns a JSON response
    # with a 'detail' key. More details in the following doc:
    # https://fastapi.tiangolo.com/tutorial/handling-errors/#the-resulting-response
    error_detail = e.value.response.json()
    assert error_detail.get('detail') == f'Invalid operation "{invalid_operation_name}"'

    print('Exception raised as expected')
