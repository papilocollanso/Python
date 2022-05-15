
import requests

class APICall:
     ''' Base class to make a basic API call with requests'''
     def call(sef, method,api_url):
         if method.lower() == 'get':
             r= requests.get(api_url)
         match r.status_code:
             case 200 | 201 | 202:
                 return r.json()['value']
             case  _:
                 raise TypeError("API error")
class ChuckNorris(APICall):
    '''This is the chuck norris api'''
    url ="https://api.chucknorris.io/jokes/random?category="
    categories =["animal","dev"]
    def __init__(self,category):
        self.category = category
        if not self.category in self.categories:
            raise TypeError("category options['animal','dev']")
    def get(self):
        api_url = f'{self.url}{self.category}'
        return self.call("GET",api_url)
    