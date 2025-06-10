import csv
def load_file(filename, ID):
    data = {}
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[row[ID]] = row
    return data
#-----------------------------------------------------------------
import random
def show_random(data):
    if type(data) == list:
        print(random.choice(data))
    else:
        print(random.choice(list(data.items())))
#-----------------------------------------------------------------
def add_file_content(filename, ID, data, name):
    for k,v in data.items():
        v[name] = ''
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        found = 0
        not_found = 0
        for row in reader:
            if row[ID] in data:
                data[row[ID]][name] += (' ' + row[name])
                found += 1
            else:
                not_found += 1
        print('Added {} fields ({} IDs not found).'.format(found, not_found))
    return data
#-----------------------------------------------------------------
def load_ratings(filename, users, restaurants):
    ratings = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if ((row['userID'] in users) and (row['placeID'] in restaurants)):
                ratings.append(row)
            else:
                print('Not found.')
    return ratings
#-----------------------------------------------------------------
def drop_fields(data, drop_list):
    for k,v in data.items():
        for e in drop_list:
            v.pop(e)
    return data
#-----------------------------------------------------------------
def encode(data, field, encode_dict):
    for k,v in data.items():
        v[field] = encode_dict[v[field].strip()]
    return data
#-----------------------------------------------------------------
def sub(time, index):
    hours = int(time[6:8]) - int(time[0:2])
    hours += (int(time[9:11]) - int(time[3:5]))/60
    if (hours < 0):
        hours += 24
    factor = 5 if (index==0) else 1;
    return hours * factor
def special_replacement(data, field):
    for k,v in data.items():
        if (field == 'days'):
            v[field] = v[field].count(';')
        elif (field == 'hours'):
            ranges = v[field].strip().split(' ')
            if (len(ranges) < 3):
                v[field] = 0
            else:
                v[field] = sum([sub(x,i) for i,x in enumerate(ranges)])
        elif (field == 'marital_status'):
            v['single'] = 1 if (v[field]=='single') else 0
            v.pop(field)
        elif (field == 'hijos'):
            v['kids'] = 1 if (v[field]=='kids') else 0
            v.pop(field)
        elif (field == 'birth_year'):
            v['age'] = 2022 - int(v['birth_year'])
            v.pop(field)
    return data
#-----------------------------------------------------------------
def rename_keys(data, old_keys, new_keys):
    for k,v in data.items():
        for old,new in zip(old_keys, new_keys):
            v[new] = v.pop(old)
    return data
#-----------------------------------------------------------------
def ratings_list_to_dict(data):
    ratings_dict = {}
    for rating in data:
        if rating['userID'] not in ratings_dict:
            ratings_dict[rating['userID']] = []
        ratings_dict[rating['userID']].append(rating)
    return ratings_dict
#-----------------------------------------------------------------
#import random
def divide_dataset(data):
    ratings_dict = ratings_list_to_dict(data)
    train = []
    validation = []
    test = []
    for k,v in ratings_dict.items():
        random.shuffle(v)
        test.append(v[0])
        validation.append(v[1])
        train.extend(v[2:])
    random.shuffle(train)
    random.shuffle(validation)
    random.shuffle(test)
    print('{} train, {} validation, {} test.'.format(
        len(train),len(validation),len(test)))
    return train, validation, test
#-----------------------------------------------------------------
import math
def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(float(x1) - float(x2),2) +
                     math.pow(float(y1) - float(y2),2))
def coincidences(Rlist, Ulist):
    Upreferences = Ulist.strip().split(' ')
    return int(any([(p in Rlist) for p in Upreferences]))
def comparison(Rdata, Udata):
    return int(Rdata == Udata)
def obtain_inputs(r, u):
    vector = []
    # relation restaurant-user -----------------------------
    vector.append(distance(r['latitude'], r['longitude'], 
                           u['latitude'], u['longitude']))
    vector.append(coincidences(r['cuisines'], u['cuisines']))
    vector.append(coincidences(r['payments'], u['payments']))
    vector.append(comparison(r['ambience'], u['ambience']))
    vector.append(r['price'])
    vector.append(u['budget'])
    vector.append(r['parking_availability'])
    vector.append(u['car_owner'])
    vector.append(r['alcohol_friendliness'])
    vector.append(u['alcohol_friendliness'])
    vector.append(r['smoking_friendliness'])
    vector.append(u['smoking_friendliness'])
    vector.append(r['dress_code'])
    vector.append(u['dress_preference'])
    # just restaurant -----------------------------------
    vector.append(r['weekly_hours'])
    vector.append(r['accessibility'])
    vector.append(r['days'])
    vector.append(r['franchise'])
    vector.append(r['other_services'])
    vector.append(r['outdoor'])
    # just user -----------------------------------------
    vector.append(u['age'])
    vector.append(u['salary'])
    vector.append(u['single'])
    vector.append(u['kids'])
    return vector
#-----------------------------------------------------------------
import numpy as np
def obtain_inputs_outputs(data, restaurants, users):
    inputs = []
    outputs1 = []
    outputs2 = []
    outputs3 = []
    for rating in data:
        inputs.append(obtain_inputs(restaurants[rating['placeID']], users[rating['userID']]))
        outputs1.append([int(rating['rating'])])
        outputs2.append([int(rating['food_rating'])])
        outputs3.append([int(rating['service_rating'])])
    return np.array(inputs), np.array(outputs1), np.array(outputs2), np.array(outputs3)
#-----------------------------------------------------------------