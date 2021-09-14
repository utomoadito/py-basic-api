from app import app

# Jika menjalankan 'python main.py' coding dibawah akan berjalan dgn port 8001
# Jika menjalankan 'flask run' maka akan berjalan secara default port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)