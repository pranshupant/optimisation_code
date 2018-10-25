import urllib.request
import urllib.parse
import re
import numpy as np
from multiprocessing import Pool

def get_Page(file_loc = 'coord_database.html'):

    url_i = 'https://m-selig.ae.illinois.edu/ads/'

    url = url_i + file_loc

    #data = urllib.parse.urlencode
    #data = data.encode('utf-8')

    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    resp_Data = resp.read()

    return resp_Data, url

#print(respData)
coord_data = []
yResult = []

respData = get_Page()
airfoils = re.findall(r'<a\s{1}href="([./A-Za-z0-9]+dat)">',str(respData))
a = str(airfoils[0])
b = a.split('.')

#urllib.request.urlretrieve(url, airfoils[i])
def save(i):
    
    coord_Data = get_Page(airfoils[i])
    urllib.request.urlretrieve(coord_Data[1], airfoils[i])

'''y = Pool(12)

yResult = y.map(save, range(len(airfoils)))'''

np.savetxt('Airfoil_list.txt', airfoils, fmt='%s')
