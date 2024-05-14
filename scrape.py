import httpx
from bs4 import BeautifulSoup


url='https://www.mcdonalds.com/us/en-us/full-menu/mccafe-coffees.html'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

}
def extract_data(data):
    try:
        #info extraction
        pass
    except Exception as e:
        print(e)

def main():
    #Get request from url
    response=httpx.get(url, headers=headers)
    #prints the html retrieved
    #print(response.text)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    #Find elems with a particular class name (returned as a list)
    print(soup.find_all(class_='classname'))

    import pdb
    pdb.set_trace()
    
if __name__=='__main__':
    main()

