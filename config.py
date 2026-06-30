import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
dbname = os.getenv("DBNAME")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
port = os.getenv("PORT")
host = os.getenv("HOST")
admin_id = os.getenv("ADMIN_ID")