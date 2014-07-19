#  python-encoding                                                                                                                                                     
 
  
This package contains a python library for working with the Encoding.com RESTful API.  
The current version supports making requests using xml/json data encoding formats.

Example usage:

    import os
    import pprint
    import encodingapi
    import lxml
    from lxml import etree
            
    encoding_instance = encodingapi.Encoding(
                                             user_id=os.getenv('ENCODING_API_USER_ID',None),
                                             user_key=os.getenv('ENCODING_API_USER_KEY',None),
                                            )

    result = encoding_instance.get_user_info()

    if encoding_instance.format == 'json':
        pprint.pprint(result)
    elif encoding_instance.format == 'xml':
        pprint.pprint(etree.tostring(result))
