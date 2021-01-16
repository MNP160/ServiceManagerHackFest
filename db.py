import pymongo

_db=None

def get_connection():
    global _db
    if not _db:
         client = pymongo.MongoClient("mongodb+srv://mnp160:pass123@cluster0.rutbx.mongodb.net/servicemanager?retryWrites=true&w=majority")
         _db=client['servicemanager']

    return _db  
         
    
     

def get_collection(collection_name):
    conn = get_connection()
    collection=conn[collection_name]
    return collection



def get_all_services():
    service_collection=get_collection('services')
    services=[]
    for document in service_collection.find():
        services.append(document)
    
    return services


def delete_service(name):
    service_collection=get_collection('services')
    deletedService=service_collection.find_one_and_delete({'name':name})
    if deletedService:
        return True
    else:
        return False


def edit_service_by_name(name, url):
    service_collection=get_collection('services')
    editedService=service_collection.find_one({'name':name})
    substr=editedService.get('_id')
    result=service_collection.find_one_and_update({'_id':substr}, {'$set':{'url':url}})
    if result:
        return True
    else:
        return False

            
def edit_service_by_url(name, url):
    service_collection=get_collection('services')
    editedService=service_collection.find_one({'url':url})
    substr=editedService.get('_id')
    result=service_collection.find_one_and_update({'_id':substr}, {'$set':{'name':name}})
    if result:
        return True
    else:
        return False
                        
   

def get_all_logs():
    logs_collection=get_collection('logs')
    logs=[]
    for document in logs_collection.find():
        logs.append(document)
    
    return logs


def check_user_exists(email, password):
    user_collection=get_collection('users')
    user=user_collection.find_one({'email':email, 'password':password})
    if user:
       return True
    else:
        return False    


#result=edit_service_by_name('testapi2', 'localhost:8083')
#print(result)

#result = delete_service("testapi3")
#print(result)
#logs=get_all_logs()
#print(logs)

#result=check_user_exists('admin@gmail.com', 'testpass')
#print(result)


#service = get_collection('services')
#print(service.find_one({}))