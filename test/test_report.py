import pytest
from crmModule.models import Report
from django.urls import reverse
from django.test import TestCase, Client
from test.factories import sponsorFactory, sponsor2Factory

class ReportTestCase(TestCase):

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
        self.firstsponsor=sponsorFactory()
        self.secondSponsor = sponsor2Factory()

    def test_getInfo(self):
        self.loginRequired()
        self.firstsponsor.save()
        self.secondSponsor.save()
        url = reverse('agreement')
        response = self.client.get(url)
        self.assertEqual(len(response.context['sponsors']),2)

    def test_agreement(self):
        self.loginRequired()
        self.firstsponsor.save()
        self.secondSponsor.save()
        url = reverse('agreement', args=[2])
        response = self.client.get(url)
        self.assertEqual(response.context['selected_sponsor'].name, self.secondSponsor.name)

