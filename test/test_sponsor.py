import pytest
from django.urls import reverse
from crmModule.models import Sponsor
from django.test import TestCase, Client
from test.factories import sponsorFactory, sponsor2Factory

class SponsorTestCase(TestCase):
        
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
        self.firstSponsor = sponsorFactory.create()
        self.secondSponsor = sponsor2Factory.create()
    
    def test_acces_sponsor(self):
        self.loginRequired()
        response = self.client.get('/sponsor/')
        self.assertHTMLEqual( response.context['template'],'sponsor.html')

    def test_error_access_sponsor(self):
        response = self.client.get('/sponsor/')
        self.assertEqual(response.status_code,302)

    def test_register_sponsor(self):
        self.loginRequired()
        data:Sponsor = {
        'name' :"Carvajal",
        'personType' : "J",
        'contact_number':"315471353",
        'email' : "Carv@gmail.com",
        'previousColab' : "si"
        }
        response = self.client.post('/sponsor/register/', data)
        self.assertEqual(Sponsor.objects.filter(name = data['name']).exists(),True)
        self.assertEqual(len(Sponsor.objects.all()),1)
    
    def test_empty_form(self):
        self.loginRequired()
        data:Sponsor = {
        'name' :"Carvajal",
        'personType' : "J",
        'contact_number':"315471353",
        'email' : "Carv@gmail.com"
        }
        response = self.client.get('/sponsor/register/', data)
        self.assertEqual(response.status_code,200)
    
    def test_register_manySponsors(self):
        self.loginRequired()
        self.firstSponsor.save()
        data:Sponsor = {
        'name' :"Tecnoquimica",
        'personType' : "J",
        'contact_number':"3187952652",
        'email' : "Tquimicas@gmail.com",
        'previousColab' : "si"
        }
        response = self.client.post('/sponsor/register/', data)
        self.assertEqual(Sponsor.objects.filter(name = data['name']).exists(),True)
        self.assertEqual(len(Sponsor.objects.all()),2)


    def test_error_register_sponsor(self):
        self.loginRequired()
        self.firstSponsor.save()
        data:Sponsor = {
        'name' :"Carvajal",
        'personType' : "J",
        'contact_number':"315471353",
        'email' : "Carv@gmail.com",
        'previousColab' : "si"
        }
        response = self.client.post('/sponsor/register/', data)
        self.assertEqual(len(Sponsor.objects.all()),1)
        self.assertEqual(response.status_code,200)

    def test__delete_sponsor(self):
        self.loginRequired()
        self.firstSponsor.save()
        self.secondSponsor.save()
        url = reverse('delete_sponsor', args=[1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual( Sponsor.objects.filter(name='Carvajal').exists(), False)
        self.assertEqual(len(Sponsor.objects.all()),1)

    def test__search_sponsor(self):
        self.loginRequired()
        self.firstSponsor.save()
        self.secondSponsor.save()
        url = reverse('sponsor_detail', args=[2])
        response = self.client.get(url)
        expectedHtml= response.context['template']
        self.assertHTMLEqual(expectedHtml,'sponsor_detail.html')
        self.assertEqual(response.context['sponsor'].name,"Manuelita")
        self.assertEqual(response.status_code,200)

    def test__update_sponsor(self):
        self.loginRequired()
        self.firstSponsor.save()
        self.secondSponsor.save()
        data:Sponsor = {
        'name' :"Carvajal",
        'personType' : "J",
        'contact_number':"315471353",
        'email' : "CarCalijal@hotmail.com",
        'previousColab' : "si"
        }
        url = reverse('update_sponsor', args=[1])
        response = self.client.post(url, data)
        self.assertEqual(Sponsor.objects.get(name='Carvajal').email,data['email'])
        self.assertEqual(len(Sponsor.objects.all()),2)

    def test__empty_update_sponsor(self):
        self.loginRequired()
        self.firstSponsor.save()
        self.secondSponsor.save()
        data:Sponsor = {
        'name' :"Carvajal",
        'personType' : "J",
        'contact_number':"315471353",
        'email' : "CarCalijal@hotmail.com",
        'previousColab' : "si"
        }
        url = reverse('update_sponsor', args=[1])
        response = self.client.get(url, data)
        self.assertFalse(Sponsor.objects.get(name='Carvajal').email==data['email'])
        self.assertEqual(len(Sponsor.objects.all()),2)

    def test__error_update_sponsor(self):
        self.loginRequired()
        self.firstSponsor.save()
        self.secondSponsor.save()
        data:Sponsor = {
        'name' :"Carvajal",
        'personType' : "J",
        'email' : "CarCalijal@hotmail.com",
        'previousColab' : "si"
        }
        url = reverse('update_sponsor', args=[1])
        response = self.client.post(url, data)
        self.assertFalse(Sponsor.objects.get(name='Carvajal').email==data['email'])
        self.assertEqual(response.context['error'],"Error updating sponsor")
        self.assertEqual(len(Sponsor.objects.all()),2)


    

