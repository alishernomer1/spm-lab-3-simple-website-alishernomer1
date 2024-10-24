from flask import Flask

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return '''
    <h1>Alisher Mubinov is Here!</h1>
    <p>This is my personal website for SPM</p>
    <a href="/about">Go to About Page</a>
    '''

# About page route
@app.route('/about')
def about():
    return '''
    <h1>About Page</h1>
    <p>Hello Professor</p>
    <a href="/">Go back to Home Page</a>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  