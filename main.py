import os

import openai
import tiktoken
from dotenv import find_dotenv, load_dotenv

import load_model
import message

_ = load_dotenv(find_dotenv())  # .env fájl olvasása

openai.api_key = os.environ["OPENAI_API_KEY"]

# message.rovid_proba()

# message.role_bemutatas()

# message.role_szoveg_hossz()

# message.role_osszesitve()

# message.token_szam()

# message.delimiter_bemutatas()

# message.moderation_bemutatas()

# message.prompt_injection_vedelem()

# message.prompt_injection_erzekeles()

# message.lanc_gondolkozas()
