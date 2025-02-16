from backend.views.text.controller import TextController


class TestTextController:
  def test_make_upper(self) -> None:
    text = 'hello'

    result = TextController.make_uppercase(text)
    assert result == 'HELLO'

  def test_make_upper_doesnt_return_lower(self) -> None:
    text = 'hello'

    result = TextController.make_uppercase(text)
    assert result != 'hello'

  def test_make_lower(self) -> None:
    text = 'HELLO'

    result = TextController.make_lowercase(text)
    assert result == 'hello'

  def test_make_lower_doesnt_return_upper(self) -> None:
    text = 'HELLO'

    result = TextController.make_lowercase(text)
    assert result != 'HELLO'

  def test_make_sentence(self) -> None:
    text = 'hello'

    result = TextController.make_sentence_case(text)
    assert result == 'Hello'

  def test_make_sentence_doesnt_return_lower(self) -> None:
    text = 'hello'

    result = TextController.make_sentence_case(text)
    assert result != 'HELLO'
    assert result != 'hello'
