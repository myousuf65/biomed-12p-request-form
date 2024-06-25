import xmlrpc.client
import base64

API_KEY = 'aa459463d1c6400ed7b7419647362dfcb2c6bfee'
URL = 'https://www.biomederp.com'
USERNAME = 'yousuf@biomed.com.hk'
PASSWORD =  'apple123@biomed'
DB_NAME = 'biomed-technology-holdings-limited1'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(URL))
print(common.version())

uid = common.authenticate(DB_NAME, USERNAME, PASSWORD, {})

if uid:
    print("authentication successful")
else:
    print("failed to authenticate")


models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(URL))

# newContact = {
#     'name' : 'test-contact-bad',
#     'street' : 'test-address',
#     'email' : 'email@example.com',
#     'mobile' : '97111233',
#     'phone' : '3134144442',
#     'type' : 'contact',
#     'company_type' : 'person', 
#     'parent_id' : '1975',                         # id of parent company
# 	# 'x_personincharger' : 'Steve Wong',
#     'x_salesperson' : 'Steve Wong',
#     'x_studio_approved_1' : True,
# }
#
# new_id = models.execute_kw(DB_NAME, uid, PASSWORD, 'res.partner', 'create', [newContact])

# 12p id =9
num = 12345567

newTask = {
    'name' : '20240988677',
	'project_id' :  9 ,
	'x_studio_surname' : 'yousuf',
	'x_studio_given_name' :  'pathan',
	'x_studio_hkid_number': 'M27876(8)',
	'x_studio_gender' :  'Male',
	'x_studio_date_of_birth' :  '2003-12-20',
	'x_studio_email' : 'yousuf@biomed.com.hk',
	'x_studio_height': 80,
	'x_studio_weight' : 78,
	'x_studio_ethnicity' : 'chinese',
	'x_studio_report_language' : 'traditional_chinese',
	'x_studio_postal_address' : 'tak tin street, chai wan',
	'x_studio_phone_number_1' : str(num),
	'x_studio_have_done_test_previously' : 'no',
	'x_studio_previous_test_date_1' : '2001-04-01' ,
	'x_studio_previous_test_name' : 'name' ,
}

new_id = models.execute_kw(DB_NAME, uid, PASSWORD, 'project.task', 'create', [newTask])
print(new_id)
