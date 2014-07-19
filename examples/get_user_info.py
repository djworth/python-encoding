#!/usr/bin/env python
import os
import pprint
import encodingapi
import pdb

if __name__ == '__main__':

    encoding_instance = encodingapi.Encoding(
                                             user_id=os.getenv('ENCODING_API_USER_ID',None),
                                             user_key=os.getenv('ENCODING_API_USER_KEY',None),
                                            )  
    print 'Grabbing user info'
    result = encoding_instance.get_user_info()
    print 'User info results:'
    
    if encoding_instance.format == 'json':
       
        pprint.pprint(result)

    elif encoding_instance.format == 'xml': 
        import lxml
        from  lxml import etree
        pprint.pprint(etree.tostring(result))

    else:
        print 'Skipping attempt to render non-registered request format'
