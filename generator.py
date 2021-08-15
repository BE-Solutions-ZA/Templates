import os
import requests
import subprocess
from dotenv import load_dotenv

load_dotenv()

# Load Api Keys

HTML_TO_PDF_API_TOKEN = os.environ.get('HTML_TO_PDF_API_TOKEN')
HTML_TO_PDF_API_ENDPOINT = 'https://api.sejda.com/v2/html-pdf'
HCTI_API_ENDPOINT = 'https://hcti.io/v1/image'
HCTI_API_USER_ID = os.environ.get('HTML_TO_IMAGE_ID')
HCTI_API_KEY = os.environ.get('HTML_TO_IMAGE_KEY')

# Open the HTML File

print("Opening the html file")

with open('templates.html', 'r') as f:
    htmlCode = f.read()

# Part 1: Generate the pdf file

# Hit the sejda api and generate Templates.pdf file

print("Genertating the PDF file from the HTML file")



r = requests.post(HTML_TO_PDF_API_ENDPOINT, json = {
    'htmlCode': htmlCode,
    'viewportWidth': 1200
  }, headers = {
    'Authorization': 'Token: {}'.format(HTML_TO_PDF_API_TOKEN)
  })
open('templates.pdf', 'wb').write(r.content)

print("Done generating templates.pdf\nOnto templates.png")

# Part 2: Generate the PNG file

# Hit the HTML to PNG API

data = { 'html': htmlCode }

image = requests.post(url = HCTI_API_ENDPOINT, data = data, auth=(HCTI_API_USER_ID, HCTI_API_KEY))

# Save the image to a PNG file

pngurl = image.json()['url'] + '.png'
pngName = 'templates.png'

print('Saving the file to ', pngName)

subprocess.call(['sh', 'downloader.sh', pngurl,pngName]) 

print('\nRe feditše, we are done!')
