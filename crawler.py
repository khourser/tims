
def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)


install_and_import('selenium')
install_and_import('csv')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import list2csv
import csvRD
import csvWR



#from bs4 import BeautifulSoup as bs
import time
# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.

#driver = webdriver.Chrome('/home/yunjy/development/python/chromedriver')
driver = webdriver.Chrome('./chromedriver/chromedriver_win32/chromedriver')
#driver = webdriver.chrome("")


#options = webdriver.ChromeOptions()
#options.add_argument('headless')
#options.add_argument('window-size=1920x1080')
#options.add_argument('disable-gpu')
#options.add_argument('user-agent=')
#driver = webdriver.Chrome('/home/yunjy/development/python/chromedriver',chrome_options=options)
# PhantomJS의 경우 | 아까 받은 PhantomJS의 위치를 지정해준다.
#driver = webdriver.PhantomJS('/home/yunjy/development/python/phantomjs')

#id = input("id: ")
#pwd =input("pw: ")
driver.implicitly_wait(3)
driver.get('https://tims.tmax.co.kr/login.html')

tmaxData='//*[@id="form"]/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/input[2]'
driver.find_element_by_xpath(tmaxData).click()

driver.find_element_by_id('userId').send_keys("")
#driver.find_element_by_name('passwd').send_keys("")
#driver.find_element_by_xpath('//*[@id="btnLogin"]').click()

#time.sleep(1)
element = WebDriverWait(driver,900).until(lambda driver:driver.find_element_by_id('frameTop'))
driver.switch_to_frame(driver.find_element_by_id('frameTop'))

driver.find_element_by_xpath('//*[@id="Image2"]').click()
driver.implicitly_wait(3)
driver.switch_to_default_content()
driver.switch_to_frame(driver.find_element_by_id('frameLeft'))
driver.find_element_by_id('menuImg213').click()
#driver.find_element_by_id('menuImg213').click()
driver.find_element_by_id('subMenuLink135')
tbodies=driver.find_elements_by_tag_name('tbody')
for tbody in tbodies:
    #print(tbody.text)
    if('근태관리' in tbody.text):
        p=tbody.find_element_by_tag_name('a')
        p.click()
        print(p.text)
spans = driver.find_elements_by_tag_name('span')
for span in spans:
    # print(tbody.text)
    if ('일일근태조회' in span.text):
        p = span.find_element_by_tag_name('a')
        p.click()
        print(p.text)
driver.implicitly_wait(3)

driver.switch_to_default_content()
driver.switch_to_frame('frameBody')
#driver.find_element_by_id('retStDate').__setattr__('value','2018.09.01')
driver.find_element_by_id('retStDate').clear()
#driver.find_element_by_id('retStDate').send_keys('2018.09.01')
driver.execute_script("document.getElementById('retStDate').value='2018.01.01'")
#driver.execute_script("document.getElementById('countPerPage').value='3'")

#driver.find_element_by_id('retStDate').click()
#driver.find_element_by_id('retStDate').send_keys(Keys.ENTER)

driver.find_element_by_id('tCountPerPage').click()
options = driver.find_elements_by_tag_name('option')
for option in options:
    if('100' in option.text):
        p = option.find_element_by_xpath('//*[@id="tCountPerPage"]/option[4]')
        driver.execute_script("document.getElementById('tCountPerPage').getElementsByTagName('option')[3].setAttribute('value','1000')")
        p.click()

elems = driver.find_elements_by_xpath('//*[@id="form"]/table[2]')
list2d=[[]]
i=0
for elem in elems:
    trs = elem.find_elements_by_tag_name('tr')
    for tr in trs:
        tds = tr.find_elements_by_tag_name('td')
        list1d = []
        for td in tds:
            td_text = td.text
            list1d.append(td_text)
        print(list1d)
        list2d.append(list1d)
        list1d = []
        #list1d[:]=[]
        #del list1d[:]
        #list1d.clear()
#list2csv.list2csv(list2d)
csvWR.csvWR(list2d)






print("==after loop==")
del list2d[0]
print(list2d)
driver.quit()
for list in list2d:
    list_split=list[9].split()

    if(len(list_split)!=1):
        del list_split[0]
        hh=list_split[0].split(':')[0]
        mm=list_split[0].split(':')[1]
        hh=int(hh)+24
        list_split=str(hh)+':'+mm
        list[9]=list_split
    else:
        continue


for list in list2d:
    print(list)

#list2csv.list2csv(list2d)






        #list_tr = tr_text.split()
#        print(type(list_tr))
#        print(list_tr)
        #list2d.append(list_tr)
#        break
#        tds=tr.find_elements_by_tag_name('td')
#        for td in tds:
#            print(td.text,end="")
#        print("")

#del list2d[0]
#for list in list2d:
#    print(list)

#for list in list2d:
#    print(list[6],'\t',list[7])



    #driver.execute_script("document.getElementById('countPerPage').value='3'")

#driver.quit()

#print(driver.find_element_by_id('135'))



