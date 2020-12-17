import os
import json
import duolingo
from dotenv import load_dotenv

# Load env variables
load_dotenv()
DUO_PASS = os.environ.get("DUO_PASS")

# All information from request
lingo = duolingo.Duolingo('maxwelldemaio', DUO_PASS)

# Get array of languages I am learning
myLangs = lingo.get_languages()

# Get all language information
myLangsInfo = []
for lang in myLangs:
    myLangsInfo.append(lingo.get_language_details(lang))

# Create JSON of language info
print(json.dumps(myLangsInfo))
