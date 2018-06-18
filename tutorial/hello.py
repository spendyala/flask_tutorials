from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/name/<username>')
def hello_user(username):
    # return 'Hello %s' % (username, ) ### Really really old formats
    # return 'Hello {}'.format(username)
    # return 'Hello {username}'.format(**{'username': username})
    return f'Hello {username}'


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=9500
    )
