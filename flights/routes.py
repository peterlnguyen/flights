from flights import app
import googleflights
print(dir(pm))

@app.route('/')
def hello_world():
    google_flights.search_flights('fizz')
    return 'Hello World!'

@app.route('/hello', methods=['POST'])
def foobar():
    return render_template('placeholder')
