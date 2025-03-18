import warnings
warnings.filterwarnings("ignore")
from crewai import Crew, Agent, Task
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY 
os.environ["OPENAI_MODEL_NAME"] = "gpt-4"

print("Hello")