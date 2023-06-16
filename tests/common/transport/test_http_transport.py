import unittest

from vectordb.common.transport.http_transport import HttpTransport

class TestHttpTransport(unittest.TestCase):
    def test_defaults(self):
        http = HttpTransport(endpoint='https://example.org:8080')
        self.assertEqual(http.user_agent, 'VectorDB Client/1.0')

