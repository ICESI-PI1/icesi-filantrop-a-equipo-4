import factory
from crmModule.models import Official, Event, Sponsor,Sponsor_Event



class sponsorFactory(factory.Factory):
    class Meta:
        model = Sponsor
    
    name = "Carvajal"
    personType = "J"
    contact_number="315471353"
    email = "Carv@gmail.com"
    previousColab = "si"

class sponsor2Factory(factory.Factory):
    class Meta:
        model = Sponsor
    
    name = "Manuelita"
    personType = "J"
    contact_number="3216852423"
    email = "ManuelIng@gmail.com"
    previousColab = "si"

class sponsor3Factory(factory.Factory):
    class Meta:
        model = Sponsor
    
    name = "Argos S.A"
    personType = "J"
    contact_number="3207258863"
    email = "argC@gmail.com"
    previousColab = "si"

class event1Factory(factory.Factory):
    class Meta:
        model = Event
    name = "Almuerzo Manuelita"
    date = "20230218"
    time = "13:00"
    event_Type = "F"

class event2Factory(factory.Factory):
    class Meta:
        model = Event
    name = "Desayuno Becados Argos"
    date = "20230615"
    time = "08:00"
    event_Type = "F"





        

