import json
import requests


class Bot:
    graph_url = 'https://graph.facebook.com/v15.0/'
    
    def __init__(self,token:str,id:str) -> None:
        self.token=token
        self.id=id