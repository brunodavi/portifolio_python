from unittest import TestCase
from unittest.mock import patch, Mock

from src.portifolio_python.lib import get_pins_from_html, get_pins_from_html_stream


class TestGetPinned(TestCase):
    @patch('requests.get')
    def test_get_titles_pinned(self, requests_get: Mock):
        requests_get().text = (
            '<div>'
            '\n\t<span class="repo" title="repo_1">repo_invalid</span>'
            '\n\t<span class="repo" title="repo_2">repo_invalid</span>'
            '\n</div>'
        )

        expected_repos = ['repo_1', 'repo_2']
        repos_pinned = get_pins_from_html('https://example.com')

        self.assertEqual(repos_pinned, expected_repos)

    @patch('requests.get')
    def test_stream_pinned_repos(self, requests_get: Mock):
        requests_get().iter_lines = Mock(return_value=[
            '<ol>',
            'class="repo"',
            '</ol>',

            '<ol>',
            '<span class="repo" title="repo_1">repo_invalid</span>',
            '<span class="repo" title="repo_2">repo_invalid</span>"',
            '</ol>',

            '<span class="repo" title="repo_invalid">repo_invalid</span>'
        ])

        expected_repos = ['repo_1', 'repo_2']
        repos_pinned = get_pins_from_html_stream('https://example.com')

        self.assertEqual(expected_repos, repos_pinned)
