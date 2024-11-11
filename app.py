from flask import Flask, jsonify
import secrets
import string

app = Flask(__name__)

@app.route('/generar_contraseña', methods=['GET'])
def generar_contraseña():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(secrets.choice(caracteres) for _ in range(12))
    return jsonify({'contraseña': contraseña})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
