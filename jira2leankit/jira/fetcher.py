"""
Fetcher classes and methods to get data out of JIRA
"""
from requests.exceptions import ConnectionError


class DoesNotExist(Exception):
    """
    Exception thrown when an object isn't found in JIRA
    """
    pass


class JIRAFetcher(object):
    """
    Handles getting data out of JIRA and returning it
    in a useful Pythonic manner
    """

    def __init__(self, server, username, password):
        """
        :param server: Full URL to the server including the protocol
        (e.g. https://jira.example.com)
        :param username: Username
        :param password: Password
        """
        self.server = server
        self.username = username
        self.password = password
        self._service = self._connect()

    def _connect(self):  # pragma: no cover
        """
        Private method for establish a connection to the JIRA api and
        populating JIRAFetcher._service
        """
        options = {
            'server': self.server,
        }
        auth = (self.username, self.password)
        from jira.client import JIRA
        return JIRA(options=options, basic_auth=auth)

    def fetch(self, key):
        """
        :param key: The JIRA unique key (e.g. PROJECT-1, SUPPORT-292)
        :return: Dictionary of data from JIRA for the issue
        :rtype: Dictionary
        :raise:
        """
        try:
            issue = self._service.issue(key)
        except ConnectionError:
            raise DoesNotExist

        return {'key': issue.key}
