import httplib, urllib
from lxml import etree

ENCODING_API_URL = 'manage.encoding.com:80'

class Encoding(object):
    
    def __init__(self, userid, userkey, url=ENCODING_API_URL):
        self.url = url
        self.userid = userid
        self.userkey = userkey

    def get_media_info(self, action='GetMediaInfo', ids=[], headers={'Content-Type':'application/x-www-form-urlencoded'}):
        query = etree.Element('query')

        nodes = {   'userid':self.userid,
                    'userkey':self.userkey,
                    'action':action,
                    'mediaid':','.join(ids),
                    }

        query = self._build_tree(etree.Element('query'), nodes) 
        
        results = self._execute_request(query, headers)

        return self._parse_results(results)

    def get_status(self, action='GetStatus', ids=[], extended='no', headers={'Content-Type':'application/x-www-form-urlencoded'}):
        query = etree.Element('query')

        nodes = {   'userid':self.userid,
                    'userkey':self.userkey,
                    'action':action,
                    'extended':extended,
                    'mediaid':','.join(ids),
                    }

        query = self._build_tree(etree.Element('query'), nodes) 
        
        results = self._execute_request(query, headers)

        return self._parse_results(results)

    def add_media(self, action='AddMedia', source=[], notify='', formats=[], instant='no', headers={'Content-Type':'application/x-www-form-urlencoded'}):

        query = etree.Element('query')

        nodes = {   'userid':self.userid,
                    'userkey':self.userkey,
                    'action':action,
                    'source':source,
                    'notify':notify,
                    'instant':instant,
                    }

        query = self._build_tree(etree.Element('query'), nodes) 
        
        for format in formats:
            format_node = self._build_tree(etree.Element('format'), format) 
            query.append(format_node)

        results = self._execute_request(query, headers)

        return self._parse_results(results)

    def _build_tree(self, node, data):
        
        for k,v in data.items():
            if isinstance(v, list):
                for item in v:
                    element = etree.Element(k)
                    element.text = item
                    node.append(element)
            else:
                element = etree.Element(k)
                element.text = v
                node.append(element)

        return node

    def _execute_request(self, xml, headers, path='', method='POST'):

        params = urllib.urlencode({'xml':etree.tostring(xml)})

        conn = httplib.HTTPConnection(self.url)
        conn.request(method, path, params, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()

        return data

    def _parse_results(self, results):
        return etree.fromstring(results)
