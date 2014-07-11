#!/usr/bin/env python
from pkgutil import extend_path                                                                                                                                                  
__path__ = extend_path(__path__, __name__)

import httplib
import urllib
import pprint
import requests

from encodingapi import connection
from encodingapi import constants
from encodingapi.request import builder

class Encoding(object):
    
    def __init__(self, 
                 user_id=None, 
                 user_key=None, 
                 request_format=constants.ENCODING_API_XML_REQUEST_FORMAT):

        self.encoding_api_connection = connection.EncodingDotComConnection(user_id=user_id,
                                                                           user_key=user_key)

        self.user_id = self.encoding_api_connection.user_id
        self.user_key = self.encoding_api_connection.user_key
        self.url = self.encoding_api_connection.url
        self.request_builder = builder.EncodingRequestBuilder(encoding_format=request_format)

        self.request_object, self.request_class = self.request_builder.build_request_object()

        
    def get_user_info(self, 
                       action='GetUserInfo', 
                       headers=constants.ENCODING_API_HEADERS):

        result = None

        nodes = {   'userid':self.user_id,
                    'userkey':self.user_key,
                    'action':action,
                    'action_user_id':self.user_id,
                    }

        if self.request_object is not None:

            self.request_object.build(nodes) 
        
            results = self._execute_request(request_obj=self.request_object, 
                                            headers=headers)
            if results is not None: 
                result = self.request_class.parse(results)

        return result

    def get_media_info(self, 
                       action='GetMediaInfo', 
                       ids=None, 
                       headers=constants.ENCODING_API_HEADERS):


        result = None

        nodes = {   'userid':self.user_id,
                    'userkey':self.user_key,
                    'action':action,
                    'mediaid':','.join(ids),
                    }

        if self.request_object is not None:

            self.request_object.build(nodes) 
        
            results = self._execute_request(request_obj=self.request_object, 
                                            headers=headers)
            if results is not None: 
                result = self.request_class.parse(results)

        return result

    def get_status(self, 
                   action='GetStatus', 
                   ids=None, 
                   extended='no', 
                   headers=constants.ENCODING_API_HEADERS):

        result = None

        nodes = {   'userid':self.userid,
                    'userkey':self.userkey,
                    'action':action,
                    'extended':extended,
                    'mediaid':','.join(ids),
                    }

        if self.request_object is not None:

            self.request_object.build(nodes) 
        
            results = self._execute_request(request_obj=self.request_object, 
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
                  headers=constants.ENCODING_API_HEADERS):

        result = None

        nodes = {   'userid':self.userid,
                    'userkey':self.userkey,
                    'action':action,
                    'source':source,
                    'notify':notify,
                    'instant':instant,
                    }

        if self.request_object is not None:

            self.request_object.build(nodes) 
        
            for format_entry in formats:

                self.request_object.append('format',
                                           format_entry)

            results = self._execute_request(request_obj=self.request_object, 
                                            headers=headers)
            if results is not None:
                result = self.request_class.parse(results)

        return result

    def transcode_asset(self,
                        transcode_job=None,
                        headers=constants.ENCODING_API_HEADERS):
        result = None

        if self.request_object is not None:

            self.request_object.build(transcode_job) 
        
            results = self._execute_request(request_obj=self.request_object, 
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
            request_params = {}
            request_params[request_obj.request_type] = request_obj.raw_form
            params = urllib.urlencode(request_params)
            conn = httplib.HTTPConnection(self.url)
            conn.request(method, path, params, headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()

        return data


