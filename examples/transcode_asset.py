#!/usr/bin/env python
import os
import json
import cStringIO
import pprint
import encodingapi
import pdb

if __name__ == '__main__':
    r_format = 'json'

    #for this example, you need to have a fully constructed
    #json-encoded transcoding job for an asset that you want
    #to transcode. if you do not have a json-encoded job file,
    #this example will not work

    if os.path.exists('./transcoding_job_json_dump.json'):

        encoding_instance = encodingapi.Encoding(
                                                 user_id=os.getenv('ENCODING_API_USER_ID',None),
                                                 user_key=os.getenv('ENCODING_API_USER_KEY',None),
                                                 request_format=r_format
                                                )  
        print 'Transcoding asset'

        with open('./transcoding_job_json_dump.json','rb') as transcode_job:
            transcode_dict = json.loads(transcode_job.read())
        result = encoding_instance.transcode_asset(transcode_dict)

        print 'Response from attempt to transcode asset:'
    
        if r_format == 'json':

            pprint.pprint(result)

        elif r_format == 'xml': 
            pprint.pprint(etree.tostring(result))

        else:
            print 'Skipping attempt to render non-registered request format'

    else:

        print 'You must have a transcoding job which has been dumped via json.dump to run this example'
