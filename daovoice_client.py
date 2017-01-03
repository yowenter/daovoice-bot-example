# -*- encoding:utf-8 -*-

import requests
import json
import config

default_headers = {'Authorization': 'token %s' % config.DAOVOICE_ACCESS_TOKEN,
                   'Content-Type': 'application/json'}


class DaoVoiceClient(requests.Session):
    '''
    http://docs.daovoice.io/api/
    DaoVoice Open API Docs.

    '''

    def __init__(self, base_url=None, timeout=10, headers=None):
        super(DaoVoiceClient, self).__init__()
        self.base_url = base_url or 'https://api.daovoice.io'
        self._timeout = timeout
        self.headers = headers or default_headers.copy()

    def _url(self, path):
        return '{0}{1}'.format(self.base_url, path)

    def _set_params(self, kwargs):
        kwargs.setdefault('timeout', self._timeout)
        headers = kwargs.get("headers", {})
        kwargs.setdefault('headers', headers)
        return kwargs

    def _post(self, url, **kwargs):
        return self.post(url, **self._set_params(kwargs))

    def _post_json(self, url, data, **kwargs):
        if 'headers' not in kwargs:
            kwargs['headers'] = {}
        kwargs['headers']['Content-Type'] = 'application/json'
        return self._post(url, data=json.dumps(data), **self._set_params(kwargs))

    def _raise_for_status(self, response):
        """
        :param response:
        :param explanation:
        :return: None
        """

        response.raise_for_status()

    def reply_conversation(self, conversation_uuid, admin_id, message_body, message_type):
        path = '/v1/conversations/%s/reply' % conversation_uuid
        data = {
            'admin': {
                'admin_id': admin_id
            },
            'message_type': message_type,
            'body': message_body
        }
        url = self._url(path)
        self._raise_for_status(self._post_json(url, data))


daovoice_client = DaoVoiceClient(base_url=config.DAOVOICE_API)


def get_daovoice_client():
    return daovoice_client
