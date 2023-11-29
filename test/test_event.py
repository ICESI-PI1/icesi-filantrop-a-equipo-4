import pytest
from crmModule.models import Event,Sponsor_Event
from django.urls import reverse
from django.test import TestCase, Client
from test.factories import event1Factory, event2Factory, sponsor2Factory, sponsor3Factory


class EventTestCase(TestCase):

    def loginRequired(self):
        data = {
        'name' :"Esteban Quintero",
        'email' : "destebanQ@gmail.com",
        'username':"esteban1",
        'password1' : "1234",
        'password2' : "1234"
        }
        response=self.client.post('/signup/',data)
        self.client.login(username="esteban1", password= "1234")

   

    def setUp(self):
        self.client=Client()
        self.firstEvent=event1Factory.create()
        self.secondEvent=event2Factory.create()
        self.firstSponsor=sponsor2Factory.create()
        self.secondSponsor=sponsor3Factory.create()
    
    def test_access_event(self):
        self.loginRequired()
        response = self.client.get('/event/')
        self.assertHTMLEqual( response.context['template'],'event.html')

    def test_error_access_event(self):
        response = self.client.get('/event/')
        self.assertEqual(response.status_code,302)

    def test_register_event(self):
        self.loginRequired()
        self.firstSponsor.save()
        data = {
        'sponsor_name': 'Manuelita',
        'participation': 'Financia',
        'name': 'Almuerzo Manuelita',
        'date': '2023-11-15',
        'time':'13:00',
        'event_Type': 'F',
        }
        response = self.client.post('/event/register/', data)
        self.assertEqual( Event.objects.filter(name=data['name']).exists(), True)
        self.assertEqual( Sponsor_Event.objects.filter(Sponsor_id__name=data['sponsor_name'], participation=data['participation']).exists(), True)
    
    def test_invalidForm(self):
        self.loginRequired()
        self.firstSponsor.save()
        data = {
        'sponsor_name': 'Manuelita',
        'name': 'Almuerzo Manuelita',
        'date': '2023-11-15',
        'time':'13:00',
        'event_Type': 'F',
        }
        response = self.client.post('/event/register/', data)
        self.assertEqual( Event.objects.filter(name=data['name']).exists(), False)
        self.assertEqual(response.context['error'],"Introduce datos válidos")
    
    def test_empty_form(self):
        self.loginRequired()
        self.firstSponsor.save()
        data = {
        'sponsor_name': 'Manuelita',
        'participation': 'Financia',
        'name': 'Almuerzo Manuelita',
        'date': '2023-11-15',
        'time':'13:00',
        'event_Type': 'F',
        }
        response = self.client.get('/event/register/', data)
        self.assertFalse(response.context['combined_form'].is_valid())
        
    def test_register_manyevents(self):
        self.loginRequired()
        self.firstEvent.save()
        self.secondSponsor.save()
        data = {
        'sponsor_name': 'Argos S.A',
        'participation': 'Invitado',
        'name': 'Desayuno Becados Argos',
        'date': '2023-06-15',
        'time':'08:00',
        'event_Type': 'F',
        }
        response = self.client.post('/event/register/', data)
        self.assertEqual( Event.objects.filter(name=data['name']).exists(), True)
        self.assertEqual( Sponsor_Event.objects.filter(Sponsor_id__name=data['sponsor_name'], participation=data['participation']).exists(), True)
        self.assertEqual(len(Event.objects.all()),2)
    
    def test_error_register_event(self):
        self.loginRequired()
        self.firstEvent.save()
        self.secondEvent.save()
        self.firstSponsor.save()
        data = {
        'sponsor_name': 'Manuelita',
        'participation': 'Invitado',
        'name': "Almuerzo Manuelita",
        'date': '2023-02-17',
        'time':'13:00',
        'event_Type': 'O',
        }
        response = self.client.post('/event/register/', data)
        self.assertEqual( Sponsor_Event.objects.filter(Sponsor_id__name=data['sponsor_name'], participation=data['participation']).exists(), False)
        self.assertEqual(len(Event.objects.all()),2)

    def test_delete_event(self):
        self.loginRequired()
        self.firstEvent.save()
        self.secondEvent.save()
        url = reverse('delete_event', args=[1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual( Event.objects.filter(name='Almuerzo Manuelita').exists(), False)
        self.assertEqual(len(Event.objects.all()),1)

    def test_search_event(self):
        self.loginRequired()
        self.firstSponsor.save()
        data = {
        'sponsor_name': 'Manuelita',
        'participation': 'Invitado',
        'name': "Almuerzo Manuelita",
        'date': '2023-02-17',
        'time':'13:00',
        'event_Type': 'O',
        }
        response = self.client.post('/event/register/', data)
        url = reverse('event_detail', args=[1])
        response2 = self.client.get(url)
        expectedHtml= response2.context['template']
        self.assertHTMLEqual(expectedHtml,'event_detail.html')
        self.assertEqual(response2.context['event'].name,"Almuerzo Manuelita")
        self.assertEqual(response2.status_code,200)

    def test_update_event(self):
        self.loginRequired()
        self.firstEvent.save()
        self.firstSponsor.save()
        data = {
        'name': "Almuerzo Manuelita",
        'date': '2023-02-17',
        'time':'17:00',
        'event_Type': 'O',
        }
        url = reverse('update_event', args=[1])
        response = self.client.post(url, data)
        self.assertEqual(Event.objects.get(name='Almuerzo Manuelita').time.strftime("%H:%M"),data['time'])

    def test_error_update_event(self):
        self.loginRequired()
        self.firstEvent.save()
        self.firstSponsor.save()
        data = {
        'name': "Almuerzo Manuelita",
        'date': '2023-02-17',
        'time':'17:00',
        }
        url = reverse('update_event', args=[1])
        response = self.client.post(url, data)
        self.assertEqual(response.context['error'],"Error updating event")
        self.assertFalse(Event.objects.get(name='Almuerzo Manuelita').time.strftime("%H:%M")==data['time'])

    def test_empty_update_event(self):
        self.loginRequired()
        self.firstEvent.save()
        self.firstSponsor.save()
        data = {
        'name': "Almuerzo Manuelita",
        'date': '2023-02-17',
        'time':'17:00',
        'event_Type': 'O',
        }
        url = reverse('update_event', args=[1])
        response = self.client.get(url, data)
        self.assertFalse(response.context['form'].is_valid())

   
