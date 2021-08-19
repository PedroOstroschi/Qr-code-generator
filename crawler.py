import requests
import hashlib
import pandas as pd
from bs4 import BeautifulSoup as Soup

#Pass the headers you want to retrieve from the xml, such as ["loc"]
def parse_sitemap( url, headers):
    resp = requests.get(url)
    #if we don`t get a valid response
    if(200 != resp.status_code):
        return False
    
    #beautifulSoup to parse the document
    soup = Soup(resp.content, "xml")

    #Find all the <url> tags in the document
    urls = soup.findAll('url')
    sitemaps = soup.findAll('sitemap')
    new_list = ["Source"] + headers
    panda_out_total = pd.DataFrame([], columns=new_list)

    #If it didn`t found any tags <url> or <sitemap>, return false
    if not url and not sitemaps:
        return False

    #Recursive call to the the function if sitemap contains sitemaps
    if sitemaps:
        for u in sitemaps:
            sitemaps_urL = u.find('loc').string
            panda_recursive = parse_sitemap(sitemaps_urL, headers)
            panda_out_total = pd.concat([panda_out_total], panda_recursive)

    # storage
    out = []

    #create a hash of the parent sitemap
    hash_sitemap = hashlib.md5(str(url).encode('utf-8')).hexdigest()

    #Extract the keys wanted
    for u in urls:
        values = [hash_sitemap]
        for head in headers:
            loc = None
            loc = u.find(head)
            if not loc:
                loc = "None"
            else:
                loc = loc.string()
            values.append(loc)
        out.
    
    
    return