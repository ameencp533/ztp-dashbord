from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True,host='100.65.212.6')

