import os
from flask import Flask, render_template, request, redirect, send_file
import xmlrpc.client
import base64
from dotenv import load_dotenv
import mysql.connector
import datetime
import pandas as pd

load_dotenv()


API_KEY = os.getenv("API_KEY")
URL = os.getenv("URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD") 
DB_NAME = os.getenv("DB_NAME")
DOMAIN = os.getenv("DOMAIN")

DB_NAME=os.getenv("DB_NAME")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_HOST=os.getenv("DB_HOST")


connector = mysql.connector.connect(
    user = DB_USER,
    password = DB_PASSWORD,
    host = DB_HOST,
    database = DB_NAME
)
cursor = connector.cursor()


common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(URL))


app = Flask(__name__)

# udomain cpanel auto route first page
@app.route('/index.php')
def redirect_to_request():
    return redirect("/request")



@app.route('/12p')
def _12p():
    return render_template("12p_form.html")


@app.route('/add-order')
def add_order():
    
    # pass query params from project code page to this page
    pc = request.args.get("pc") 
    pn = request.args.get("pn")
    sal = request.args.get("sal")
    
    return render_template("add_order.html", pc=pc,pn=pn, sal=sal)

@app.route("/serial_num")
def serial_num():
    
    values = {}
   
    cursor.execute("SELECT * FROM serial_number_storage")
    nums = cursor.fetchall()
    connector.commit()
    print(nums)
    for item in nums:
        values[item[1]] = item[2]     # type: ignore
    print(values)

    return render_template("serial_number.html", values=values)


@app.route('/add-order', methods = ['POST'])
def submitorder():
    
    order_type = request.form['order_type']
    route = request.form['route']
    quantity = request.form['quantity']
    project_code = request.form['project_code']
    customer = request.form["customer"]
    dn_number = request.form["dn-number"]

    yy = str(datetime.datetime.now().year)
    yy = yy[2:4]
    mm = datetime.datetime.now().month
    mm = "{:02d}".format(mm)

    tt = ''
    sn = ""

    if order_type == '16s_oral' or order_type == '16s_gut':
        tt = '1'
        cursor.execute('SELECT val FROM serial_number_storage where id=1')
        sn = cursor.fetchone()[0]
        connector.commit()
            
        new_val = tuple()
        if sn is not None:
            new_val = (int(sn), int(quantity))
            nv = sum(new_val)
            cursor.execute('UPDATE serial_number_storage SET val= %s where id=1', [int(nv)])
            connector.commit() 
    
    elif order_type == '7p' or order_type == '11p' or order_type == '12p' or order_type == '13p' or order_type == 'obesity' or order_type == 'immunity':
        tt = '2'
        cursor.execute('SELECT val FROM serial_number_storage where id=2')
        sn = cursor.fetchone()[0]
        connector.commit()
        new_val = tuple()
        if sn is not None:
            new_val = (int(sn), int(quantity))
            nv = sum(new_val)
            cursor.execute('UPDATE serial_number_storage SET val= %s where id=2', [int(nv)])
            connector.commit()  
    elif order_type == 'petcare':
        tt = '3'
        cursor.execute('SELECT val FROM serial_number_storage where id=5')
        sn = cursor.fetchone()[0]
        new_val = tuple()
        if sn is not None:
            new_val = (int(sn), int(quantity))
            nv = sum(new_val)
            cursor.execute('UPDATE serial_number_storage SET val= %s where id=5', [int(nv)])
            connector.commit() 
    elif order_type == 'platinum':
        tt = '5'
        cursor.execute('SELECT val FROM serial_number_storage where id=3')
        sn:int = cursor.fetchone()[0]
        connector.commit()
        new_val = tuple()
        if sn is not None:
            new_val = (int(sn), int(quantity))
            nv = sum(new_val)
            cursor.execute('UPDATE serial_number_storage SET val= %s where id=3', [int(nv)])
            connector.commit() 
     
    counter = 1 
    all_test_urls = []
    all_test_nums = []
    
    for test_kit_number in range(sn, sn+int(quantity) ):
        sum_val = int(sn)+counter
        s = "{:03d}".format(sum_val)
        test_kit_number = yy+mm+tt+str(s)
        
        all_test_urls.append(DOMAIN+order_type+"?name="+test_kit_number)
        all_test_nums.append(test_kit_number)
        
        today = datetime.datetime.now()
        # Format the date as 'yy-mm-dd'
        formatted_date = today.strftime('%y-%m-%d')
        # Return as a datetime object
        order_date = datetime.datetime.strptime(formatted_date, '%y-%m-%d')
        
        cursor.execute("INSERT INTO project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) values (%s, %s, %s, %s, %s, %s)", (project_code, yy+mm+tt+str(s), route, order_date, customer, dn_number ))
        counter += 1
    
    
    connector.commit()
    
    file_data = {
        "URLs" : all_test_urls,
        "Test Kit Numbers" : all_test_nums,
    }
    
    print("===================data============",file_data)
    
    df = pd.DataFrame(file_data)
    df.to_excel("kit_urls.xlsx", index=False)
    
    return send_file("kit_urls.xlsx", as_attachment=True)
    


@app.route('/submit-details', methods=['POST'])
def post_details():
    uid = common.authenticate(DB_NAME, USERNAME, PASSWORD, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(URL))
    formdata = request.form



    test_kit_id = formdata['name']
    surname = formdata['surname']
    given_name= formdata['given_name']
    full_name = formdata['surname'] + " " + formdata['given_name']
    hkid_number= formdata['hkid_number']
    passport_number = formdata['passport_number']
    chinese_name=  formdata['chinese_name']
    date_of_birth = formdata['date_of_birth']
    gender = formdata['gender']
    phone_number = formdata['phone_number']
    n_ethnicity = formdata['ethnicity']
    ethnicity = str(n_ethnicity[0])
    email = formdata['email']
    weight = formdata['weight']
    height = formdata['height']
    postal_address = formdata['postal_address']
    postal_code = formdata['postal_code']
    medical_history = formdata['medical_history']
    previous_test = formdata.get('previous_test', '')
    previous_test_date = formdata.get('previous_test_date', '')
    previous_test_name = formdata.get('previous_test_performed', '')
    parent_name = formdata.get('parent_name', '')
    parent_hkid = formdata.get('parent_hkid', '')
    report_language = formdata['report_language']        
  
    # cursor.reset()
    cursor.execute('SELECT project_id FROM project_test_link where test_kit_id=%s', [test_kit_id])
    project_id = cursor.fetchone()
    

    if project_id == None:
        return "the test kit number is not valid"
    

    project_id = str(project_id[0])        

    cursor.execute('''
        SELECT patientid from patients
        WHERE hkid=%s 
        OR date_of_birth=%s
    ''', [formdata['hkid_number'], formdata['date_of_birth']] )
    patient_id = cursor.fetchone()
   

    if patient_id == None:
        cursor.execute('SELECT val FROM serial_number_storage WHERE id=6')
        fetched_num = int(cursor.fetchone()[0])+1
        patient_id = "P"+str(fetched_num)
        
        cursor.execute('UPDATE serial_number_storage SET val=%s WHERE id=6', [fetched_num] )
        connector.commit()
    
     
        cursor.execute('''
            INSERT INTO patients (
                patientid,
                lastname,
                firstname,
                fullname,
                hkid,
                passport_number,
                chinese_name,
                date_of_birth,
                gender,
                mobile,
                ethnicity,
                email,
                weight,
                height,
                address1,
                postal_code,
                medical_history
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', [
            patient_id,
            surname,
            given_name,
            full_name,
            hkid_number,
            passport_number,
            chinese_name,
            date_of_birth,
            gender,
            phone_number,
            ethnicity,
            email,
            weight,
            height,
            postal_address,
            postal_code,
            medical_history
        ])
        connector.commit()
    else:
        patient_id = patient_id[0]

    newTask = {
        'name' : test_kit_id ,
        'project_id' :  9 ,
        'x_studio_test_kit_id': test_kit_id,
        'x_studio_surname' : surname,
        'x_studio_given_name' :  given_name,
        'x_studio_hkid_number': hkid_number,
        'x_studio_passport_number' : passport_number,
        'x_studio_gender' : gender,
        'x_studio_date_of_birth' :  date_of_birth,
        'x_studio_email' : email,
        'x_studio_height': height,
        'x_studio_weight' : weight,
        'x_studio_ethnicity' : ethnicity,
        'x_studio_report_language' : report_language,
        'x_studio_postal_address' : postal_address,
        'x_studio_phone_number_1' : str(phone_number),
        'x_studio_have_done_test_previously' : previous_test ,
        'x_studio_previous_test_date' :  previous_test_date ,
        'x_studio_previous_test_name' : previous_test_name ,
        'x_studio_parent_name' : parent_name,
        'x_studio_parent_hkid' : parent_hkid,
        'x_studio_patient_id' : patient_id,
        'x_studio_project_code' : project_id,

    }
    
    print(newTask)
    new_id = models.execute_kw(DB_NAME, uid, PASSWORD, 'project.task', 'create', [newTask])

    if isinstance(new_id, int):
        return render_template("12pnext.html", test_kit_id=test_kit_id)

@app.route("/check-status", methods=['GET','POST'])
def checkstatus():
    if request.method == "POST":
        
        FORM_RECIEVED = "request_form_received"
        SPECIMEN_REJECTED = "rejected"
        SPECIMEN_RECIEVED = "specimen_received"
        REPORT_READY = "report_ready"

        # odoo auth
        uid = common.authenticate(DB_NAME, USERNAME, PASSWORD, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(URL))
        
        kitNumber = request.form['test-kit-number']
        query = models.execute_kw(DB_NAME, uid , PASSWORD,  'project.task', 'search', [[['name', '=', kitNumber ]]])
        retrievedRecord = models.execute_kw(DB_NAME, uid , PASSWORD,  'project.task', 'read', [query], {'fields' : ['stage_id']})
        
        STAGE = ""
        for record in retrievedRecord:
            print(record)
            if record['stage_id'][0] == 52:
                STAGE = FORM_RECIEVED 
                print(STAGE)
            elif record["stage_id"][0] == 63:
                STAGE = SPECIMEN_REJECTED
            elif record['stage_id'][0] == 53:
                STAGE = SPECIMEN_RECIEVED
            elif record["stage_id"][0] == 54:
                STAGE = REPORT_READY

        return render_template("order-status.html", stage=STAGE)        
    return render_template("input-test-kit.html")

@app.route("/test", methods=["GET",])
def index():
    status = 'specimen_received'  # This would be dynamically set
    return render_template('order-status.html', status="report_ready")

@app.route("/12p-questions", methods=['GET'])
def _12pquestions():
    return render_template("12p_questionnaire.html")
#
@app.route("/7p-questions", methods=['GET'])
def _7pquestions():
    return render_template("7p_questionnaire.html")

@app.route("/project_code", methods=['GET'])
def project_code():


    #TODO:  pagination
    
    cursor.execute('SELECT * FROM project_code')
        
    rows = cursor.fetchall()
    connector.commit()
    return render_template("project_code.html", data=rows)

@app.route("/submit-questions", methods=['POST'])
def submit_questions():
    data = request.form
    cursor.execute('''
        INSERT INTO q_answers (
            test_kit_id,
            question1,
            question2,
            question3,
            question4,
            question5,
            question6,
            question7,
            question8,
            question9,
            question10,
            question11,
            question12,
            question13,
            question14,
            question15,
            question16,
            question17

        ) values (
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
        ) 
    ''', [ 
        data['test_kit_id'],
        data['question1'],
        data['question2'],
        data['question3'],
        data['question4'],
        data['question5'],
        data['question6'],
        data['question7'],
        data['question8'],
        data['question9'],
        data['question10'],
        data['question11'],
        data['question12'],
        data['question13'],
        data['question14'],
        data['question15'],
        data['question16'],
        data['question17']
    ])
    connector.commit()
    # return an answer confirmation page
    return render_template("12pend.html")

@app.route('/error')
def test():
    return render_template('error.html')

@app.route('/all_orders')
def allorders():
    cursor.execute('SELECT * FROM project_test_link')
    allorders = cursor.fetchall()
    connector.commit()
    return render_template("project_test_link.html", allorders=allorders)

@app.route("/survey")
def survey():
    cursor.execute('SELECT * FROM q_answers')
    all_ans = cursor.fetchall()
    print(all_ans)
    
    return render_template("allsurvey.html", all_ans = all_ans)

@app.route('/reset-serial')
def resetSerial():
    cursor.execute('''
                UPDATE serial_number_storage
                SET val = 0
                WHERE id IN (1, 2, 3, 4, 5);
                    ''')
    connector.commit()
    return redirect("/serial_num")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
