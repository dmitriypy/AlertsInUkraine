# AlertsInUkraine
Unofficial API for alerts.in.ua in Python

Get key
-----

To get the key, send an e-mail (a@dun.ai) or a message in Telegram (@andunai). To speed up the receipt of the key, add the hashtag “#api” to the text of your message.

Usage
-----
        
**Get id**

    from alerts_in_ukraine import States
    
    print(repr(States.Dnipropetrovsk))
    
    <States.Dnipropetrovsk: 3>
    
**Get all id's**

    from alerts_in_ukraine import AlertsAPI
    
    key = input("Your key: ")
    id = int(input("Your id: "))
    
    siren = AlertsAPI(key, id)
    print(siren.get_alert())
    
    Your key: mykey
    Your id: 0
    
    {
    "states": [
        {
        "id": 1,
        "name": "Вінницька область",
        "name_en": "Vinnytsia oblast",
        "alert": false,
        "changed": "2022-04-05T06:12:52+03:00"
        },
        {
        "id": 2,
        "name": "Волинська область",
        "name_en": "Volyn oblast",
        "alert": false,
        "changed": "2022-04-05T06:13:06+03:00"
        },
        # ...
    ],
    "last_update": "2022-04-05T06:15:10.333210918+03:00"
    }

**Get information about a place**
    
    from alerts_in_ukraine import AlertsAPI
    
    key = input("Your key: ")
    id = int(input("Your id: "))
    
    siren = AlertsAPI(key, id)
    print(siren.get_alert())
    
    Your key: mykey
    Your id: 3
    
    {
    "state": {
        "id": 3,
        "name": "Дніпропетровська область",
        "name_en": "Dnipropetrovsk oblast",
        "alert": false,
        "changed": "2022-04-05T06:13:12+03:00"
    },
    "last_update": "2022-04-05T06:15:10.333210918+03:00"
    }

License
-------

MIT license
