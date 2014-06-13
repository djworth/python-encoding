#!/usr/bin/env python

import os
import httplib
import urllib
import json
import lxml
from lxml import etree
import pprint
import pdb
import requests

"""
This framework relies on the following environment variables
being available. Otherwise, the variables that make use of them
are set to None

ENCODING_API_REQUEST_FORMAT = 'json'
ENCODING_API_HOST = 'manage.encoding.com'
ENCODING_API_PORT = '80'
ENCODING_API_USER_ID = <encoding.com-user-id>
ENCODING_API_USER_SECRET = <encoding.com-secret-key>

"""

#Encoding.com request constants
ENCODING_API_URL_TEMPLATE = '{}:{}'
ENCODING_API_REQUEST_TYPE = 'query'
ENCODING_API_HEADERS = { 
                        'Content-Type':'application/x-www-form-urlencoded',
                       }

def build_url(host=None,
              port=None):

    url_host = os.getenv('ENCODING_API_HOST',None) or host
    url_port = os.getenv('ENCODING_API_PORT',None) or port

    return ENCODING_API_URL_TEMPLATE.format(url_host,
                                            url_port)

class XmlRequest(object):

    def __init__(self):
        self.request = etree.Element(ENCODING_API_REQUEST_TYPE)
        self.request_type = 'xml'

    @property
    def query(self):
        return self.request

    @property
    def type(self):
        return self.request_type

    @property
    def raw_form(self):
        return etree.tostring(self.request)

    def prepare_request(self,
                        data=None):

        return self.build(data=data)

    def build(self, 
              data=None):
        
        if data is not None:

            for k,v in data.items():
                if isinstance(v, list):
                    for item in v:
                        element = lxml.etree.Element(k)
                        element.text = item
                        self.request.append(element)
                else:
                    element = lxml.etree.Element(k)
                    element.text = v
                    self.request.append(element)

        return self.request

    def append(self,
               node_name=None,
               node_value=None):

        if all([
               node_name is not None,
               node_value is not None,
               ]):

            new_node = lxml.etree.Element(node_name)
            new_node.text = node_value
            self.request.append(new_node)

    @staticmethod
    def parse(source=None):

        result = None

        if source is not None:
            result = lxml.etree.fromstring(source)

        return result 

class JsonRequest(object):

    def __init__(self):

        self.request = {}
        self.request[ENCODING_API_REQUEST_TYPE] = {}
        self.request_type='json'
    
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
                    self.request[ENCODING_API_REQUEST_TYPE][k] = v

        return self.request

    @staticmethod
    def parse(source=None):

        result = None

        if source is not None:
            result = json.loads(source)

        return result 


class Encoding(object):
    
    def __init__(self, 
                 userid=None, 
                 userkey=None, 
                 url=None,
                 encoding=None):

        self.url = build_url() or url
        self.userid = os.getenv('ENCODING_API_USER_ID',None) or userid
        self.userkey = os.getenv('ENCODING_API_USER_SECRET',None) or userkey

        encoding_format = os.getenv('ENCODING_API_REQUEST_FORMAT','xml')

        if encoding_format == 'xml':

            self.request_class = XmlRequest
            self.request = self.request_class()
        elif encoding_format == 'json':
            self.request_class = JsonRequest 
            self.request = self.request_class()
        else:
            self.request_class = None
            self.request = None

    def get_user_info(self, 
                       action='GetUserInfo', 
                       headers=ENCODING_API_HEADERS):

        result = None

        nodes = {   'userid':self.userid,
                    'userkey':self.userkey,
                    'action':action,
                    'action_user_id':self.userid,
                    }

        if self.request is not None:

            self.request.build(nodes) 
        
            results = self._execute_request(request_obj=self.request, 
                                            headers=headers)
            if results is not None: 
                result = self.request_class.parse(results)

        return result

    def get_media_info(self, 
                       action='GetMediaInfo', 
                       ids=None, 
                       headers=ENCODING_API_HEADERS):


        result = None

        nodes = {   'userid':self.userid,
                    'userkey':self.userkey,
                    'action':action,
                    'mediaid':','.join(ids),
                    }

        if self.request is not None:

            self.request.build(nodes) 
        
            results = self._execute_request(request_obj=self.request, 
                                            headers=headers)
            if results is not None: 
                result = self.request_class.parse(results)

        return result

    def get_status(self, 
                   action='GetStatus', 
                   ids=None, 
                   extended='no', 
                   headers=ENCODING_API_HEADERS):

        result = None

        nodes = {   'userid':self.userid,
                    'userkey':self.userkey,
                    'action':action,
                    'extended':extended,
                    'mediaid':','.join(ids),
                    }

        if self.request is not None:

            self.request.build(nodes) 
        
            results = self._execute_request(request_obj=self.request, 
                                            headers=headers)
            if results is not None:
                result = self.request_class.parse(results)

        return result

    def add_media(self, 
                  action='AddMedia', 
                  source=None, 
                  notify='', 
                  formats=None,
                  instant='no', 
                  headers=ENCODING_API_HEADERS):

        result = None

        nodes = {   'userid':self.userid,
                    'userkey':self.userkey,
                    'action':action,
                    'source':source,
                    'notify':notify,
                    'instant':instant,
                    }

        if self.request is not None:

            self.request.build(nodes) 
        
            for format_entry in formats:

                self.request.append('format',
                                    format_entry)

            results = self._execute_request(request_obj=self.request, 
                                            headers=headers)
            if results is not None:
                result = self.request_class.parse(results)

        return result

    def _execute_request(self, 
                         method='POST',
                         path='',
                         request_obj=None, 
                         headers=None):
        data = None

        if all([
                path is not None,
                headers is not None,
                request_obj is not None,
               ]):

            request = {}
            request[request_obj.type] = request_obj.raw_form
            params = urllib.urlencode(request)
            conn = httplib.HTTPConnection(self.url)
            conn.request(method, path, params, headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()

        return data

if __name__ == '__main__':

    encoding_instance = Encoding()
    print 'Grabbing user info'
    result = encoding_instance.get_user_info()
    print 'User info results:'
    
    r_format = os.getenv('ENCODING_API_REQUEST_FORMAT','xml')

    if r_format == 'json':

        pprint.pprint(result)

    elif r_format == 'xml': 
        pprint.pprint(etree.tostring(result))
    else:
        print 'Skipping attempt to render non-registered request format'
