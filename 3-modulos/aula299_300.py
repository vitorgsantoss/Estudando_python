from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv('BD_USER'))
print(os.getenv('BD_PASSWORD'))
print(os.getenv('BD_PORT'))
print(os.getenv('BD_HOST'))
