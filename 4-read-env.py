# pip install python-dotenv
from dotenv import load_dotenv
import os

          #(override=True) #yliajaa ymp.muuttujat
load_dotenv() # lukee .env -tiedoston
              # mikäli ko.ympäristömuuttujaa ei ole
              # tai sitä ei yliajeta

#load_dotenv(path_to_env_file)          

print(os.getenv("PASSWORD"))
PORT = os.getenv("PORT")
