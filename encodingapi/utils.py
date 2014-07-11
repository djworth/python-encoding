#!/usr/bin/env python
from encodingapi import constants

def build_api_url(host_name=None,
                  host_port=None):
    """
     use the provided host and port 
     to build an url string
    """

    constructed_url_string = None

    if all([host_name is not None,
            host_port is not None]):

        constructed_url_string = constants.ENCODING_API_URL_TEMPLATE.format(host_name,
                                                                            host_port)  
    return constructed_url_string
