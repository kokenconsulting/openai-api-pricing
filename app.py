from flask import Flask
import get_price 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/openai')
def getOpenAIPricing():
    return get_price.main()

result = get_price.main()
print(result)