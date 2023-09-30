import pywhatkit as pw
from googlesearch import search
from selenium import webdriver
import time
# from selenium.webdriver.common.keys import Keys


# def abcd(sitename):
#     pw.search(sitename)

def xyz(p):
    if (c == 1):
        print("Top 10 results are:")
        cnt=0
        for url in search(p):
            cnt+=1
            print(url)
            if cnt==10:
                break
    else:
        abcd(p)
def abcd(sitename):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.youtube.com/")
    driver.find_element("name", "q").send_keys(str(sitename))
    time.sleep(3)
    driver.find_element("name", "q").send_keys(Keys.ENTER)
    time.sleep(2000)
    driver.close()


while True:
    print("1.site\n2.inurl\n3.intitle\n4.intext\n5.filetype\n6.cache\n7.site:cache\n8.site:inurl")
    a = int(input("Which operator do you want to use?(enter serial number): "))
    b = str(input("What is the topic of search: "))
    c = int(input("To print websites press 1\nTo open browser press 2\n=>"))

    if (a == 1):
        h = "site:" + b
        xyz(h)
    elif (a == 2):
        h = "inurl:"+ b
        xyz(h)
    elif (a == 3):
        h = "intitle:" + b
        xyz(h)
    elif (a == 4):
        h = "intext:" + b
        xyz(h)
    elif(a == 5):
       h = "filetype:" + b
       xyz(h)
    elif (a == 6):
       h = "cache:" + b
       xyz(h)
    elif(a==7):
        h = "site:cache:" + b
        xyz(h)
    elif(a==8):
        h = "site:inurl:" + b
        xyz(h)
    else:
        print("You are continuing without operator")
        xyz(b)
    cont=input("Do you want to search again?(y/n):")
    if(cont in ["n" ,'N',"NO",'No',"no"]):
        break