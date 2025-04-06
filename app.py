from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def tour_page():
    return render_template('tour.html')

@app.route('/abbey')
def abbey():
    return render_template('abbey_falls.html')

@app.route('/dubare')
def dubare():
    return render_template('dubare.html')

@app.route('/mallali')
def mallali():
    return render_template('mallali_falls.html')

@app.route('/mandalpatti')
def mandalpatti():
    return render_template('mandalpatti.html')

@app.route('/nisargadhama')
def nisargadhama():
    return render_template('nisargadhama.html')

@app.route('/raja')
def raja():
    return render_template('rajas_seat.html')

@app.route('/talakaveri')
def talakaveri():
    return render_template('talakaveri.html')


app.run()