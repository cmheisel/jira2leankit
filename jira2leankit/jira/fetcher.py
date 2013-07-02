"""
Fetcher classes and methods to get data out of JIRA
"""
from requests.exceptions import ConnectionError


class DoesNotExist(Exception):
    pass


class JIRAFetcher(object):
    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password
        self._service = self._connect()

    def _connect(self):
        options = {
            'server': self.server,
        }
        auth = (self.username, self.password)
        from jira.client import JIRA
        return JIRA(options=options, basic_auth=auth)

    def fetch(self, key):
        try:
            issue = self._service.issue(key)
        except ConnectionError:
            raise DoesNotExist

        return {'key': issue.key}
