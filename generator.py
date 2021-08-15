import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Load Api Key

token = os.environ.get("HTMLTOPDF_API_TOKEN")

# Open the HTML File

with open('templates.html', 'r') as f:
    htmlCode = f.read()

# Hit the api and generate Templates.pdf file

url = 'https://api.sejda.com/v2/html-pdf'
r = requests.post(url, json = {
    'htmlCode': htmlCode,
    'viewportWidth': 1200
  }, headers = {
    'Authorization': 'Token: {}'.format(token)
  })
open('templates.pdf', 'wb').write(r.content)