#!/usr/bin/env python

import json

from encodingapi import constants
from encodingapi.request import base

class JsonRequest(base.EncodingRequest):

    def __init__(self):

        self.request = {}
        self.request_type = constants.ENCODING_API_JSON_REQUEST_FORMAT
        self.request[constants.ENCODING_API_REQUEST_TYPE] = {}

    @property
    def query(self):
        return self.request

    @property
    def type(self):
        return self.request_type

    @property
    def raw_form(self):
        return json.dumps(self.request)

    def prepare_request(self,
                        data=None):

        return self.build(data=data)

    def build(self, 
              data=None):

        if data is not None:

            for k,v in data.items():
                    self.request[constants.ENCODING_API_REQUEST_TYPE][k] = v

        return self.request

    def append(self,
               name=None,
               value=None):
        
        if all([
               name is not None,
               value is not None,
               ]):

            self.request[name]=value

    
    @staticmethod
    def parse(source=None):

        result = None

        if source is not None:
            result = json.loads(source)

        return result 
