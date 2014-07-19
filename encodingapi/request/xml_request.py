#!/usr/bin/env python

import lxml
import lxml.etree

from encodingapi import constants
from encodingapi.request import base

class XmlRequest(base.EncodingRequest):

    def __init__(self):
        self.request_type = constants.ENCODING_API_XML_REQUEST_FORMAT
        self.request = lxml.etree.Element(constants.ENCODING_API_REQUEST_TYPE)

    @property
    def query(self):
        return self.request

    @property
    def type(self):
        return self.request_type

    @property
    def raw_form(self):
        return lxml.etree.tostring(self.request)

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
               name=None,
               value=None):

        if all([
               name is not None,
               value is not None,
               ]):

            new_node = lxml.etree.Element(name)
            new_node.text = value
            self.request.append(new_node)

    @staticmethod
    def parse(source=None):

        result = None

        if source is not None:
            result = lxml.etree.fromstring(source)

        return result 
