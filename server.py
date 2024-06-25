from flask import Flask, render_template, request
import xmlrpc.client
import base64


API_KEY = 'aa459463d1c6400ed7b7419647362dfcb2c6bfee'
URL = 'https://www.biomederp.com'
USERNAME = 'yousuf@biomed.com.hk'
PASSWORD =  'apple123@biomed'
DB_NAME = 'biomed-technology-holdings-limited1'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(URL))



app = Flask(__name__)

@app.route('/')
def home():
    return render_template("form.html")


@app.route('/submit-details', methods=['POST'])
def post_details():
    uid = common.authenticate(DB_NAME, USERNAME, PASSWORD, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(URL))
    formdata = request.form

    print(formdata['date_of_birth'])

    newTask = {
        'name' : formdata['name'] ,
        'project_id' :  9 ,
        'x_studio_surname' : formdata['surname'],
        'x_studio_given_name' :  formdata['given_name'],
        'x_studio_hkid_number': formdata['hkid_number'],
        'x_studio_passport_number' : formdata['passport_number'],
        'x_studio_gender' : formdata['gender'],
        'x_studio_date_of_birth' :  formdata['date_of_birth'],
        'x_studio_email' : formdata['email'],
        'x_studio_height': float(formdata['height']),
        'x_studio_weight' : float(formdata['weight']),
        'x_studio_ethnicity' : formdata['ethnicity'],
        'x_studio_report_language' : formdata['report_language'],
        'x_studio_postal_address' : formdata['postal_address'],
        'x_studio_phone_number_1' : str(formdata['phone_number']),
        'x_studio_have_done_test_previously' : formdata['previous_test'] ,
        'x_studio_previous_test_date' :  formdata['previous_test_date'] ,
        'x_studio_previous_test_name' : formdata['previous_test_performed'] ,
        'x_studio_parent_name' : formdata['parent_name'],
        'x_studio_parent_hkid' : formdata['parent_hkid']
    }
    print(newTask)
    new_id = models.execute_kw(DB_NAME, uid, PASSWORD, 'project.task', 'create', [newTask])
    
    if isinstance(new_id, int):
        return "form submitted successfully"
    # return "hi"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
