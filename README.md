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
    
**Get information about a place**
    
    from AlertsInUkraine import AlertsAPI
    
    key = input("Your key: ")
    id = int(input("Your id: "))

    siren = AlertsAPI(key, id)
    print(siren.get_alerts())
        

License
-------

MIT license
