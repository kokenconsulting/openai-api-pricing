from flask import Flask
import get_price 
from pricing import calc

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/openai')
def getOpenAIPricing():
    return get_price.main()

#initial run
get_price.main()