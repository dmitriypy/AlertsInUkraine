# AlertsInUkraine
Unofficial API for alerts.in.ua in Python

Get key
-----

To get the key, send an e-mail (a@dun.ai) or a message in Telegram (@andunai). To speed up the receipt of the key, add the hashtag “#api” to the text of your message.

Usage
-----
        
**Get id**

    from AlertsInUkraine import States
    
    print(repr(States.Dnipropetrovsk))
    <States.Dnipropetrovsk: 3>
**Get information about a place**
    
    from AlertsInUkraine import AlertsAPI
    
    key = input("Your key: ")
    id = int(input("Your id: "))

    siren = AlertsAPI(key, id)
    print(siren.get_alert())
    {'state': {'id': 3, 'name': 'Дніпропетровська область', 'name_en': 'Dnipropetrovsk oblast', 'alert': False, 'changed': '2022-07-18T09:54:05+03:00'}, 'last_update': '2022-07-18T11:18:08.04873156Z'}

License
-------

MIT license
