#!/usr/bin/env python
from abc import ABCMeta, abstractmethod 
from encodingapi import constants

class EncodingRequest(object):

    __metaclass__ = ABCMeta

    def __init__(self):

        self.request_type = None
        self.request = None

    @abstractmethod
    def prepare_request(self,
                        data=None):
        pass
    
    @abstractmethod
    def build(self, 
              data=None):
        
        pass

    @abstractmethod
    def append(self,
               name=None,
               value=None):
    
        pass
