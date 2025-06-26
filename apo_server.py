from flask import Flask, request, jsonify
from apo_quantum_logos import UnifiedAPOQuantumLogos

app = Flask(__name__)

# Initialize the ΑΠΩ system
apo = UnifiedAPOQuantumLogos()

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    text = data.get('text', '')
    try:
        result = apo.process_unified_logos(text)
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    # Simple example: accept any non-empty username/password
    if username and password:
        return jsonify({'success': True, 'message': 'Login successful'})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
