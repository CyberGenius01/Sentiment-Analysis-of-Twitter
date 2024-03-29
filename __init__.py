from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '2defb92db2ee38c31da8aa03a2d53e28432f3ea3c0b301971b0c11cce102'

from model import routes