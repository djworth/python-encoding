#!/usr/bin/env python

import httplib
import urllib
import os
import requests
import json
import lxml

ENCODING_API_REQUEST_TYPE = 'query'
ENCODING_API_HOST = 'manage.encoding.com'
ENCODING_API_PORT = '80'
ENCODING_API_URL_TEMPLATE = 'http://{}:{}'
ENCODING_API_HEADERS = { 
                        'Content-Type':'application/x-www-form-urlencoded',
                       }

def build_url(host=None,
              port=None):

    url_host = host or ENCODING_API_HOST
    url_port = port or ENCODING_API_PORT

    return ENCODING_API_URL_TEMPLATE.format(url_host,
                                            url_port)


class XmlRequest(object):

    def __init__(self,
                 request_type=ENCODING_API_REQUEST_TYPE):
 
        self.request = lxml.etree.Element(request_type)

    @property
    def query(self):
        return self.request

    def prepare_request(self,
                        data=None):

        return self._build(data=data)

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
    def parse(self, 
              source=None):

        result = None

        if source is not None:
            result = lxml.etree.fromstring(source)

        return result 

class JsonRequest(object):

    def __init__(self):

        self.request = {}

class Encoding(object):
    
    def __init__(self, 
                 userid=None, 
                 userkey=None, 
                 url=None):

        self.url = url or build_url()
        self.userid = userid
        self.userkey = userkey

    def get_media_info(self, 
                       action='GetMediaInfo', 
                       ids=None, 
                       headers=ENCODING_API_HEADERS):

        xml_request = XmlRequest()

        nodes = {   'userid':self.userid,
                    'userkey':self.userkey,
                    'action':action,
                    'mediaid':','.join(ids),
                    }

        xml_request.build(nodes) 
        
        results = self._execute_request(xml_request.query, 
                                        headers)

        return XmlRequest.parse(results)

    def get_status(self, 
                   action='GetStatus', 
                   ids=None, 
                   extended='no', 
                   headers=ENCODING_API_HEADERS):

        xml_request = XmlRequest()

        nodes = {   'userid':self.userid,
                    'userkey':self.userkey,
                    'action':action,
                    'extended':extended,
                    'mediaid':','.join(ids),
                    }

        xml_request.build(nodes) 
        
        results = self._execute_request(xml_request.query, 
                                        headers)

        return XmlRequest.parse(results)

    def add_media(self, 
                  action='AddMedia', 
                  source=None, 
                  notify='', 
                  formats=None,
                  instant='no', 
                  headers=ENCODING_API_HEADERS):

        xml_request = XmlRequest()

        nodes = {   'userid':self.userid,
                    'userkey':self.userkey,
                    'action':action,
                    'source':source,
                    'notify':notify,
                    'instant':instant,
                    }

        xml_request.build(nodes) 
        
        for format_entry in formats:

            xml_request.append('format',
                               format_entry)

        results = self._execute_request(xml_request.query, 
                                        headers)

        return self._parse_results(results)

    def _execute_request(self, xml, headers, path='', method='POST'):

        params = urllib.urlencode({'xml':lxml.etree.tostring(xml)})

        conn = httplib.HTTPConnection(self.url)
        conn.request(method, path, params, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()

        return data
