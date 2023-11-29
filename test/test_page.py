# from django.test import LiveServerTestCase
# import pytest
# from crmModule.models import Official
# from django.test import TestCase

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# import time



# driver_path = r"C:\Users\jufep\Downloads\chromedriver_win32\chromedriver.exe"

# class HostTest(LiveServerTestCase):
    

#     def testSignUp(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument('--start-maximized')
#         driver = webdriver.Chrome(options=options)
#         driver.get('http://127.0.0.1:8000/signup')

#         nombre = driver.find_element(By.NAME,'name')
#         nombre.send_keys('Juan')

#         correo = driver.find_element(By.NAME,'email')
#         correo.send_keys('jufeplasa@hotmail.com')

#         user = driver.find_element(By.NAME,'username')
#         user.send_keys('jufeplasa')

#         password1 = driver.find_element(By.NAME,'password1')
#         password1.send_keys('juan123')

#         password2 = driver.find_element(By.NAME,'password2')
#         password2.send_keys('juan123')

#         WebDriverWait(driver, 5)\
#             .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
#                                                         'button.btn.btn-primary'))).click()
#     def testLogin(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument('--start-maximized')
#         driver = webdriver.Chrome(options=options)
#         driver.get('http://127.0.0.1:8000')

#         user = driver.find_element(By.NAME,'username')
#         user.send_keys('jufeplasa')

#         password1 = driver.find_element(By.NAME,'password')
#         password1.send_keys('juan123')

#         WebDriverWait(driver, 5)\
#             .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
#                                                         'button.btn.btn-primary'))).click()
        
#     def testRegisterSponsor(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument('--start-maximized')
#         driver = webdriver.Chrome(options=options)
#         driver.get('http://127.0.0.1:8000/sponsor/register')

#         name = driver.find_element(By.NAME,'name')
#         name.send_keys('Carvajal')

#         type = driver.find_element(By.NAME,'personType')
#         type.send_keys('JURIDICA')

#         contact = driver.find_element(By.NAME,'contact_number')
#         contact.send_keys('Carvajal')

#         email = driver.find_element(By.NAME,'email')
#         email.send_keys('jufeplasa@hotmail.com')

#         colab = driver.find_element(By.NAME,'previousColab')
#         colab.send_keys('si')

#         WebDriverWait(driver, 5)\
#             .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
#                                                         'button.btn.btn-primary'))).click()
#         driver.get('http://127.0.0.1:8000/sponsor/1/')
#         time.sleep(3) 


#     def testRegisterEvent(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument('--start-maximized')
#         driver = webdriver.Chrome(options=options)
#         driver.get('http://127.0.0.1:8000/event/register/')

#         name = driver.find_element(By.NAME,'name')
#         name.send_keys('Almuerzo Carvajal')

#         date = driver.find_element(By.NAME,'date')
#         date.send_keys('01/11/2023')

#         day = driver.find_element(By.NAME,'time')
#         day.send_keys('01:30')

#         type = driver.find_element(By.NAME,'event_Type')
#         type.send_keys('FLORECIMIENTO')

#         sponsor = driver.find_element(By.NAME,'sponsor_name')
#         sponsor.send_keys('Carvajal')


#         participation = driver.find_element(By.NAME,'participation')
#         participation.send_keys('invitado')

#         time.sleep(2)

#         WebDriverWait(driver, 5)\
#             .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
#                                                         'button.btn.btn-primary'))).click()
        
#         driver.get('http://127.0.0.1:8000/event/1/')
#         time.sleep(1)
        


   