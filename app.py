from flask import Flask, request, jsonify
from vdotformula import calculate_vdot_from_time

app = Flask(__name__)

@app.route('/calculate-vdot', methods=['POST'])
def calculate_vdot():
    try:
        data = request.get_json()
        time_in_seconds = data.get('time')
        if time_in_seconds is None:
            return jsonify({'error': 'Invalid input'}), 400
        
        # Calculate VDOT
        vdot = calculate_vdot_from_time(time_in_seconds)
        if vdot is None:
            return jsonify({'error': 'Calculation failed'}), 500
        
        return jsonify({'vdot': vdot})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
