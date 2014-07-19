#Encoding.com request constants
#request formats
ENCODING_API_XML_REQUEST_FORMAT = 'xml'
ENCODING_API_JSON_REQUEST_FORMAT = 'json'
#host name - api endpoint which is provided by encoding.com
ENCODING_API_HOSTNAME = 'manage.encoding.com'
#host port - api port which is utilized by encoding.com
ENCODING_API_HOST_PORT = '80'
#user id - user id that is provided by encoding.com and linked to your account
ENCODING_API_USER_ID = '<encoding.com-user-id>'
#user key - user key that is provided by encoding.com and linked to your account
ENCODING_API_USER_KEY = '<encoding.com-secret-key>'
#url template - string-based template that will be used to build api request urls
#pattern: {<HOST_NAME>:<HOST_PORT>}
ENCODING_API_URL_TEMPLATE = '{}:{}'
#request type - encoding.com sets this to query for xml/json-based api requests
ENCODING_API_REQUEST_TYPE = 'query'
#api headers - basic set of headers that will not change during encoding.com api request sessions
ENCODING_API_HEADERS = {}
ENCODING_API_HEADERS['Content-Type'] = 'application/x-www-form-urlencoded'
