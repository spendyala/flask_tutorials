from flask import Flask, request
import json

app = Flask(__name__)


# This is GET example
@app.route('/')
def hello():
    return 'Hello World!'

# This is GET example
@app.route('/name/<username>')
def hello_user(username):
    # return 'Hello %s' % (username, ) ### Really really old formats
    # return 'Hello {}'.format(username)
    # return 'Hello {username}'.format(**{'username': username})
    return f'Hello {username}'

# This is GET example
@app.route('/f_to_c/help')
def fahrenheit_to_celsius_help():
    return 'Converts Temperatures from Fahrenheit to Celsius'


def f_to_c_conversion(temp_f):
    try:
        temp_c = ((int(temp_f) - 32) * 5)/9
        return str(temp_c), True
    except TypeError as type_err:
        return 'There is Type error, input value is not converted to Integer', False
    except ValueError as val_err:
        return f'Given value to convert from Fahrenheit to Celsius is not a valid integer {temp_f}', False
   


# This is GET example
@app.route('/f_to_c/<temp_f>')
def fahrenheit_to_celsius_convert(temp_f):
    value, flag = f_to_c_conversion(temp_f)
    if flag:
       return value
    else:
       return value, 500


# This is POST example
@app.route('/f_to_c/', methods=['POST'])
def fah_to_cel_conv_post():
    import ipdb; ipdb.set_trace()
    if request.method == 'POST':
        value, flag = f_to_c_conversion(request.get_data())
        if flag:
           return value
        else:
           return value, 500
    else:
        return 'This is an invalid request', 500


# This is POST JSON example
@app.route('/f_to_c_json', methods=['POST'])
def fah_to_cel_conv_post_json():
    if request.method == 'POST':
        import ipdb; ipdb.set_trace()
        json_data = request.get_json()
        print(json_data)
        value, flag = f_to_c_conversion(json_data.get('fahrenheit'))
        if flag:
           return json.dumps({'celsius': value})
        else:
           return value, 500
    else:
        return 'This is an invalid request', 500



if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=9500
    )
