DATABASE_FILENAME = 'database.txt'


class Database:
  @staticmethod
  def write(content: str) -> None:
    with open(DATABASE_FILENAME, 'w') as file:
      file.write(content)

  @staticmethod
  def read() -> str:
    with open(DATABASE_FILENAME, 'r') as file:
      return file.read()
