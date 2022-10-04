from .models import Train
import requests

# call the mbta api
# if id is already in database, update values with new values from api
# otherwise make new object and save to database

def ping_mbta_api():
    route_0 = requests.get('https://api-v3.mbta.com/vehicles/?filter%5Broute_type%5D=0').json()
    route_1 = requests.get('https://api-v3.mbta.com/vehicles/?filter%5Broute_type%5D=1').json()
    route_0 = route_0['data']
    route_1 = route_1['data']
    route_combined = route_0 + route_1
    return route_combined

def update_train_info():
    trains = ping_mbta_api()
    if not trains:
        return
    for train in trains:
        train_id = train['id']
        train_info = train['attributes']
        route_id = train['relationships']['route']['data']['id']
        try: 
            stop_id = train['relationships']['stop']['data']['id']
        except:
            stop_id = None
        train_db = Train.objects.filter(id=train_id)
        if not train_db:
            new_train = Train(
                id=train_id, 
                line=route_id, 
                longitude=train_info['longitude'], 
                latitude=train_info['latitude'], 
                bearing=train_info['bearing'],
                status=train_info['current_status'],
                stop=stop_id) # stop name
            new_train.save()
        else:
            train_db.update(
                longitude=train_info['longitude'],
                latitude=train_info['latitude'],
                bearing=train_info['bearing'],
                status=train_info['current_status'],
                stop=stop_id
            )