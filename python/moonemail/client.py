"""Small ergonomic layer over the generated public API."""
from collections.abc import Mapping
from typing import Any
from moonemail.api_client import ApiClient
from moonemail.configuration import Configuration
from moonemail.api.emails_api import EmailsApi
from moonemail.api.domains_api import DomainsApi
from moonemail.api.inboxes_api import InboxesApi
from moonemail.api.receiving_api import ReceivingApi
from moonemail.api.api_keys_api import APIKeysApi
from moonemail.api.webhooks_api import WebhooksApi
from moonemail.api.suppressions_api import SuppressionsApi
from moonemail.api.permissions_api import PermissionsApi
from moonemail.models.send_email_request import SendEmailRequest

class Emails(EmailsApi):
    def send(self, payload: Mapping[str, Any] | SendEmailRequest, *, idempotency_key: str | None = None, timeout: float = 30):
        body = payload if isinstance(payload, SendEmailRequest) else SendEmailRequest.from_dict(dict(payload))
        return self.send_email(body, idempotency_key=idempotency_key, _request_timeout=timeout)

class Moonemail:
    """Synchronous server-side client; no automatic retries. Use as a context manager."""
    def __init__(self, api_key: str, *, base_url: str = 'https://api.moonemail.co'):
        if not api_key or not api_key.strip():
            raise ValueError('A Moonemail API key is required.')
        config = Configuration(host=base_url.rstrip('/'), access_token=api_key)
        config.retries = 0
        self.api_client = ApiClient(config)
        self.emails = Emails(self.api_client)
        self.domains = DomainsApi(self.api_client)
        self.inboxes = InboxesApi(self.api_client)
        self.receiving = ReceivingApi(self.api_client)
        self.api_keys = APIKeysApi(self.api_client)
        self.webhooks = WebhooksApi(self.api_client)
        self.suppressions = SuppressionsApi(self.api_client)
        self.permissions = PermissionsApi(self.api_client)

    def close(self):
        self.api_client.rest_client.pool_manager.clear()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
