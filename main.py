print('Hello from responsitory!')
from dotenv import load_dotenv
import os

def print_author():
    load_dotenv()
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")

# Вызываем функцию — теперь код внутри неё выполнится
print_author()
