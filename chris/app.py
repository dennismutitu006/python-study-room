from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data
admin_info = {
    'name': 'Chris',
    'phone': '0759291164'
}

predictions = [
    {'fixture': 'Team A vs Team B', 'prediction': 'Team A will win'},
    {'fixture': 'Team C vs Team D', 'prediction': 'Team D will win'},
]

@app.route('/')
def home():
    return render_template('index.html', admin_info=admin_info)

@app.route('/predictions')
def get_predictions():
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)

