#!/usr/bin/env python

from encodingapi import constants
from encodingapi.request import (
                              xml_request,
                              json_request
                             )

class EncodingRequestBuilder(object):

    def __init__(self,
                 encoding_format=constants.ENCODING_API_XML_REQUEST_FORMAT):

        self.__request_format_to_use = encoding_format


    def build_request_object(self):
        
        request_class = None
        request_object = None

        if self.__request_format_to_use == constants.ENCODING_API_XML_REQUEST_FORMAT:

            request_class = xml_request.XmlRequest
            request_object = request_class()

        elif self.__request_format_to_use == constants.ENCODING_API_JSON_REQUEST_FORMAT:

            request_class = json_request.JsonRequest 
            request_object = request_class()

        return (request_object, request_class)
