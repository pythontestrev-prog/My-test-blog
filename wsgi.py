from waitress import serve
from main import app  # Esto importa tu variable 'app' desde main.py

if __name__ == '__main__':
    print("Servidor Waitress corriendo en http://localhost:8080")
    serve(app, host='0.0.0.0', port=8080)