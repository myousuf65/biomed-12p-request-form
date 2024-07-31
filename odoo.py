import xmlrpc.client
from dotenv import load_dotenv
import os


load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = os.getenv("URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD") 
DB_NAME = os.getenv("DB_NAME")
DOMAIN = os.getenv("DOMAIN")


common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(URL))


uid = common.authenticate(DB_NAME, USERNAME, PASSWORD, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(URL))

query = models.execute_kw(DB_NAME, uid , PASSWORD,  'project.task', 'search', [[['name', '=', "SXa" ]]])

retrievedRecord = models.execute_kw(DB_NAME, uid , PASSWORD,  'project.task', 'read', [query] )
print(retrievedRecord)