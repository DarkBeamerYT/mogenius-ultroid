import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://github.com/TeamUltroid/Ultroid && cd Ultroid && pip3 install -r requirements.txt && pip3 install -r re*/st*/op* && curl -s -O https://$GIT_TOKEN@raw.githubusercontent.com/$GIT_URL && python3 -m pyUltroid &")
