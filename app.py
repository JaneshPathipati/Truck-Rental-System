from flask import Flask, render_template, jsonify, request 

app = Flask(__name__)

# Sample truck data
trucks = [
    {"id": 1, "number": "TRK101", "driver": "John Doe", "condition": "Good", "rent": "$500/day"},
    {"id": 2, "number": "TRK102", "driver": "Mike Smith", "condition": "Excellent", "rent": "$600/day"},
    {"id": 3, "number": "TRK103", "driver": "Alex Brown", "condition": "Average", "rent": "$400/day"},
    {"id": 4, "number": "TRK104", "driver": "Steve White", "condition": "Good", "rent": "$550/day"},
    {"id": 5, "number": "TRK105", "driver": "Emma Davis", "condition": "Excellent", "rent": "$700/day"},
    {"id": 6, "number": "TRK106", "driver": "James Wilson", "condition": "Good", "rent": "$650/day"},
    {"id": 7, "number": "TRK107", "driver": "Olivia Johnson", "condition": "Fair", "rent": "$350/day"},
    {"id": 8, "number": "TRK108", "driver": "Sophia Martinez", "condition": "Good", "rent": "$500/day"},
    {"id": 9, "number": "TRK109", "driver": "William Brown", "condition": "Excellent", "rent": "$750/day"},
    {"id": 10, "number": "TRK110", "driver": "Liam Garcia", "condition": "Good", "rent": "$550/day"},
]

@app.route('/')
def home():
    return render_template('index.html', trucks=trucks)

@app.route('/get_truck_details/<int:truck_id>')
def get_truck_details(truck_id):
    truck = next((t for t in trucks if t['id'] == truck_id), None)
    return jsonify(truck) if truck else (render_template('404.html'), 404)

@app.route('/truck/<int:truck_id>')
def truck_details(truck_id):
    truck = next((t for t in trucks if t['id'] == truck_id), None)
    if truck:
        return render_template('truck_details.html', truck=truck)
    return render_template('404.html'), 404

# New Route for Booking Details Page
@app.route('/booking_details', methods=['GET'])
def booking_details():
    truck_id = request.args.get('truck_id')
    truck = next((t for t in trucks if str(t['id']) == truck_id), None)
    if truck:
        return render_template('booking_details.html', truck=truck)
    return render_template('404.html'), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
