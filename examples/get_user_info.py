#!/usr/bin/env python
import os
import pprint
import encodingapi
import pdb

if __name__ == '__main__':

    r_format = 'json'
    encoding_instance = encodingapi.Encoding(
                                             user_id=os.getenv('ENCODING_API_USER_ID',None),
                                             user_key=os.getenv('ENCODING_API_USER_KEY',None),
                                             request_format=r_format
                                            )  
    print 'Grabbing user info'
    result = encoding_instance.get_user_info()
    print 'User info results:'
    
    if r_format == 'json':

        pprint.pprint(result)

    elif r_format == 'xml': 
        pprint.pprint(etree.tostring(result))
    else:
        print 'Skipping attempt to render non-registered request format'
