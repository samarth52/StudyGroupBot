import pymongo
import urllib.parse

mongo_client = pymongo.MongoClient(f"mongodb+srv://test:test@studygroup.bysjx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mongo_client.StudyGroup
collection = db.study_groups

def insert_study_group(name, course, east_west, location, now_later, time, max_number_of_people, to_do_list, channel_name):
    newDict = {'name': name, 'course': course, 'east_west': east_west, 'location': location, 'now_later': now_later,
        'time': time, 'current_number_of_people': 1, 'max_number_of_people': max_number_of_people, 'to_do_list': to_do_list,
        'channel_name': channel_name}
    collection.insert_one(newDict)

def match_study_group(name, course, east_west, location, now_later, time, max_number_of_people):
    fieldList = []
    to_add = ''
    for parameter in ['name', 'course', 'east_west', 'location', 'now_later', 'time', 'max_number_of_people']:
        value = f'{eval(parameter)}'
        if value != 'None':
            if parameter == 'time':
                fieldList.append(f"'time': {{'$gte': '{value}'}}") #Need to test this
            else:
                fieldList.append(f"'{parameter}': " + (f"{value}" if value.isdigit() else f"'{value}'"))

    command = eval("{" + ', '.join(fieldList) + "}")
    return list(collection.find(command, {'_id': 0}))

def change_num_people(name, is_increment):
    to_add = 1 if is_increment else -1
    collection.update({'name': name}, {'$inc': {'current_number_of_people': to_add}}
)

def get_names():
    result = collection.find({}, {'name': 1, '_id': 0})
    names = []
    for dictionary in result:
        names.append(dictionary['name'])

    return names

def get_course():
    return ['CS 1100', 'CS 1301', 'CS 1331', 'MATH 1551', 'MATH 1552', 'MATH 1554']

def get_to_do_list(name):
    to_do_list = list(collection.find({'name': name}, {'_id': 0, 'to_do_list': 1}))[0]['to_do_list']
    return to_do_list

def update_to_do_list(channel_name, to_do_list):
    collection.update_one({'channel_name': channel_name}, {'$set': {'to_do_list': to_do_list}})
    return len(to_do_list)

def find_channel_record(channel_name):
    record = collection.find_one({'channel_name': channel_name}, {'_id': 0})
    if record == None:
        return None
    return record['to_do_list']
