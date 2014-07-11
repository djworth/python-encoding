#  python-encoding                                                                                                                                                     
 
  
This package contains a python library for working with encoding.com.  

Example usage:


import encoding

ENCODING_USERID = '1234'
ENCODING_USERKEY = 'ABC123'


MEDIA_IN_S3 = 's3://<aws_access_key>:<aws_secret>@s3.amazonaws.com/<bucket_name>/<key>'

FORMAT = {  'output':'vp6_flix',
            'vp6_profile':'2',
            'file_extension':'flv',
            'upct':'90', 
            'size':'0x480',
            'bitrate':'256k',
            'audio_bitrate':'64k',
            'audio_sample_rate':'44100',
            'audio_channels_number':'2',
            'keyframe':'6', 
            'two_pass':'yes',
            'keep_aspect_ratio':'yes', 
            'rotate':'def',
            'kfinttype':'2',
            'cxmode':'1'
            }

encoder = encoding.Encoding(ENCODING_USERID, ENC0DING_USERKEY)
response = encoder.add_media(source=[MEDIA_IN_S3], formats=[FORMAT])

print response

