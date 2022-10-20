from dotenv import load_dotenv
import os

load_dotenv()
naverId = os.environ.get("X-Naver-Client-Id")
naverSecret = os.environ.get("X-Naver-Client-Secret")
