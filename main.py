from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import string


options = webdriver.ChromeOptions()
options.add_argument('proxy-server=173.192.21.89:80')
print('Welcome to the Panera account generator')
brt = (input('What day is your birthday?(mm/dd) '))

#random email generator
rndltr = []
while (len(rndltr) < 5):
  rndltr1 = random.choice(string.ascii_lowercase)
  rndltr.append (rndltr1)

while (len(rndltr) < 8):
  rndltr2 = str(random.randint(0, 9))
  rndltr.append (rndltr2)
  
rndltr = ''.join(rndltr)
rndltr = rndltr+'@aol.com'
print (rndltr)

#random phone number generator
phnum = []
while (len(phnum) < 10):
  rndnum = random.choice(string.digits)
  phnum.append (rndnum)

phnum = ''.join(phnum)

#first name
fstnm = rndltr[0]

#last name
lstnm = rndltr[1]

#pass
passw= 'freepanera1!'

#PATH = 'C:\Program Files (x86)\chromedriver.exe'
#driver = webdriver.Chrome(PATH)
driver = uc.Chrome(options=options,)
driver.get("https://www.panerabread.com/content/panerabread_com/en-us/mypanera/sign-up-with-mypanera.html?showSignUpForm=true&intcmp=link-g-mypanera-signup-OP1800C")

fnme = driver.find_element(By.ID,'firstName')
fnme.send_keys(fstnm)

lsnm = driver.find_element (By.ID,'lastName')
lsnm.send_keys(lstnm)

phn = driver.find_element (By.ID,'phone')
phn.send_keys(phnum)

eml = driver.find_element(By.ID,'email')
eml.send_keys(rndltr)

psw = driver.find_element (By.ID,'sign-up-password')
psw.send_keys(passw)

btd = driver.find_element(By.ID,'birthday')
btd.send_keys(brt)
btd.send_keys(Keys.RETURN)