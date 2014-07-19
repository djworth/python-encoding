#!/usr/bin/env python

from encodingapi import constants
from encodingapi import utils

"""
The encoding.com api relies on the user providing the following:

* user-id <e.g 9928> 
* user-key <e.g. a12bddef-abbd123-a221233>

These can be found by logging into the encoding.com dashboard.

Additionally, the user can set the type of api request encoding to use.

This is set to xml by default but the user can pass the request type to 
the build_request method of the EncodingDotComRequestManager class to 
have it construct json requests.

Currently, xml and json are the only request encoding types that are
understood by the encoding.com api

"""

class EncodingDotComConnection(object):

    def __init__(self,
                 user_id=None,
                 user_key=None):

        self._user_id = user_id
        self._user_key = user_key
        self.host_name = constants.ENCODING_API_HOSTNAME
        self.host_port = constants.ENCODING_API_HOST_PORT
        self.__construct_url_string(self.host_name,
                                    self.host_port)

    def __construct_url_string(self,
                               host_name=None,
                               host_port=None):

        self.__api_url =  utils.build_api_url(host_name=host_name,
                                              host_port=host_port)

    @property
    def user_id(self):
        return self._user_id

    @property
    def user_key(self):
        return self._user_key

    @property
    def url(self):
        return self.__api_url
