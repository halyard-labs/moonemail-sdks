import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from moonemail import Moonemail
from moonemail.exceptions import ApiException

class TransportTests(unittest.TestCase):
    def setUp(self):
        self.calls = []
        self.status = 200
        self.response = {'id': 'email-1'}
        owner = self
        class Handler(BaseHTTPRequestHandler):
            def handle_request(self):
                length = int(self.headers.get('Content-Length', 0))
                owner.calls.append((self.path, self.headers, json.loads(self.rfile.read(length)) if length else None))
                self.send_response(owner.status)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Retry-After', '5')
                self.end_headers()
                self.wfile.write(json.dumps(owner.response).encode())
            do_GET = do_POST = do_DELETE = handle_request
            def log_message(self, *args): pass
        self.server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.client = Moonemail('test_key', base_url=f'http://127.0.0.1:{self.server.server_port}')
    def tearDown(self):
        self.client.close()
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()
    def test_send_wire(self):
        for to in ['user@example.com', ['user@example.com']]:
            payload = {'from': 'sender@example.com', 'to': to, 'subject': 'Hello', 'text': 'Body', 'reply_to': 'reply@example.com'}
            result = self.client.emails.send(payload, idempotency_key='stable-key')
            self.assertEqual(result.id, 'email-1')
            path, headers, body = self.calls[-1]
            self.assertEqual(path, '/emails')
            self.assertEqual(headers['Authorization'], 'Bearer test_key')
            self.assertEqual(headers['Idempotency-Key'], 'stable-key')
            self.assertEqual(body, payload)
    def test_nulls_unknown_fields(self):
        self.response = {'permission': 'full_access', 'scopes': ['emails:send'], 'domain_id': None, 'expires_at': None, 'can_manage_api_keys': True, 'billing_requires_owner': True, 'future_field': 1}
        value = self.client.permissions.get_permissions()
        self.assertIsNone(value.domain_id)
        self.assertEqual(value.to_dict()['future_field'], 1)
    def test_pagination_and_encoding(self):
        self.response = {'object': 'list', 'data': [], 'has_more': False}
        self.client.emails.list_emails(limit=2, after='cursor/+')
        from urllib.parse import parse_qs, urlsplit
        self.assertEqual(parse_qs(urlsplit(self.calls[0][0]).query)['after'], ['cursor/+'])
        self.response = {'object': 'suppression', 'email': 'a+b@example.com', 'deleted': True}
        self.client.suppressions.remove_suppression('a+b@example.com')
        self.assertEqual(self.calls[1][0], '/suppressions/a%2Bb%40example.com')
    def test_no_automatic_retry(self):
        self.status = 429
        self.response = {'statusCode': 429, 'name': 'rate_limit_exceeded', 'message': 'Slow down'}
        with self.assertRaises(ApiException) as error:
            self.client.emails.send({'from': 'a@example.com', 'to': 'b@example.com', 'subject': 's', 'text': 't'})
        self.assertEqual(error.exception.status, 429)
        self.assertEqual(error.exception.headers['Retry-After'], '5')
        self.assertEqual(len(self.calls), 1)

if __name__ == '__main__': unittest.main()
