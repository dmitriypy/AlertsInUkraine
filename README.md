# AlertsInUkraine
Unofficial API for alerts.in.ua in Python

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
