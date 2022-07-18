# AlertsInUkraine
Unofficial SDK for alerts.in.ua in Python, that i made with my Capybara <3

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
    
    siren = AlertsAPI(key)
    print(siren.get_alert())
    
    Your key: mykey
    
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

**Get history about alerts**

    from AlertsInUkraine import AlertsAPI
    
    key = input("Your key: ")

    siren = AlertsAPI(key)
    print(siren.alerts_history())
    
    [
    {"id":1,"date":"2022-03-15T18:02:56+02:00","state_id":9,"alert":false},
    {"id":2,"date":"2022-03-15T18:10:34+02:00","state_id":1,"alert":true},
    {"id":3,"date":"2022-03-15T18:11:25+02:00","state_id":5,"alert":true},
    {"id":4,"date":"2022-03-15T18:15:11+02:00","state_id":10,"alert":true},
    {"id":5,"date":"2022-03-15T18:17:28+02:00","state_id":8,"alert":true},
    {"id":6,"date":"2022-03-15T18:17:29+02:00","state_id":12,"alert":true},
    {"id":7,"date":"2022-03-15T18:18:35+02:00","state_id":16,"alert":true},
    {"id":8,"date":"2022-03-15T18:19:13+02:00","state_id":2,"alert":true},
    {"id":9,"date":"2022-03-15T18:19:20+02:00","state_id":25,"alert":true},
    {"id":10,"date":"2022-03-15T18:22:29+02:00","state_id":18,"alert":true},
    {"id":11,"date":"2022-03-15T18:30:17+02:00","state_id":24,"alert":true},
    # ...
    ]
License
-------

MIT license
