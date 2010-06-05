
from urllib2 import urlopen, Request
from base64 import encodestring
from xml.dom import minidom

class Stat(object):
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url

    def _get_xml_document(self):
        headers = {
            'Accept': 'application/xml',
            'Authorization': 'Basic %s' % (
                encodestring('%s:%s' % (self.username, self.password))[:-1]
            )
        }

        req = Request(self.url, headers=headers)
        res = urlopen(req)

        return res.read()

    def get_sources(self):
        data = []

        doc = minidom.parseString(self._get_xml_document())
        icestats = doc.getElementsByTagName('icestats')[0]

        for source in icestats.getElementsByTagName('source'):
            data.append({
                'server_name': source.getElementsByTagName('server_name')[0].firstChild.data,
                'server_type': source.getElementsByTagName('server_type')[0].firstChild.data,
                'listenurl': source.getElementsByTagName('listenurl')[0].firstChild.data,
            })

        return data

