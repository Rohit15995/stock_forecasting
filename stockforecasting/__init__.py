from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '3b12c2baf6785a2bf2bb769a2113a62e'

from stockforecasting import routes