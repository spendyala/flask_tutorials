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
        json_data = request.get_json()
        print(json_data)
        value, flag = f_to_c_conversion(json_data.get('fahrenheit'))
        if flag:
           return json.dumps({'celsius': value})
        else:
           return value, 500
    else:
        return 'This is an invalid request', 500


# This is POST JSON with Multiple Fahrenheits example
@app.route('/fs_to_cs_json', methods=['POST'])
def fahs_to_cels_conv_post_json():
    if request.method == 'POST':
        json_data = request.get_json()
        print(json_data)
        fahrenheits_list = json_data.get('fahrenheits')
        celsius_list = []
        for each_f in fahrenheits_list:
            value, flag = f_to_c_conversion(each_f)
            celsius_list.append(value)
        return json.dumps({'celsius': celsius_list})
    else:
        return 'This is an invalid request', 500


# This is POST JSON with Multiple Fahrenheits example
@app.route('/fs_to_cs_easy', methods=['POST'])
def fahs_to_cels_conv_easy():
    if request.method == 'POST':
        json_data = request.get_json()
        print(json_data)
        fahrenheits_list = json_data.get('fahrenheits')
        results_list = []
        for each_f in fahrenheits_list:
            value, flag = f_to_c_conversion(each_f)
            results_list.append({'fahrenheit': each_f, 'celsius': value})
        return json.dumps({'result': results_list})
    else:
        return json.dumps({'error': 'This is an invalid request'}), 500


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=9500
    )
