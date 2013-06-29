"""
Fetcher classes and methods to get data out of JIRA
"""


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
        issue = self._service.issue(key)
        return {'key': issue.key}
