# Secure Password Generator (Python)

A Python API that generates secure passwords.

## Deployment with Docker
```bash
docker build -t password-generator .
docker run -p 5000:5000 password-generator

Access the API at:
http://127.0.0.1:5000/generar_contraseña
