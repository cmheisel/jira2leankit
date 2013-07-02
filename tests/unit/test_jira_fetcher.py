"""
JIRAFetcher tests
"""
import pytest

from core import TestCase
from mockito import when, mock


class JIRAFetcherTests(TestCase):
    """Tests for the JIRAFetcher class"""

    def _get_target_class(self):
        """Returns target class"""
        from jira2leankit.jira.fetcher import JIRAFetcher
        return JIRAFetcher

    def _make_one(self):
        """Creates a valid instance of the class under test"""
        JF = self._get_target_class()
        self.mockJIRAService = mock()
        when(JF)._connect().thenReturn(self.mockJIRAService)
        jf = JF(
            'http://jira.example.com/',
            'username',
            'password',
        )
        return jf

    def test_fetch_returns_the_tickets_data(self):
        """The fetch method should return the actual
        data of the ticket"""

        jf = self._make_one()

        mockIssue = mock()
        mockIssue.key = "CMSPD-494"
        when(self.mockJIRAService).issue("CMSPD-494").thenReturn(mockIssue)

        ticket = jf.fetch("CMSPD-494")
        assert ticket['key'] == "CMSPD-494"

    def test_fetch_raises_exception_for_missing_tickets(self):
        """
        The fetch method should raise an exception if the card doesn't
        exist in JIRA
        """
        from jira2leankit.jira.fetcher import DoesNotExist
        from requests.exceptions import ConnectionError

        jf = self._make_one()
        when(self.mockJIRAService).issue("CMSNO-1").thenRaise(ConnectionError)

        with pytest.raises(DoesNotExist):
            jf.fetch("CMSNO-1")
