from re import findall
from functools import cache


import requests


@cache
def get_pins_from_html(url: str):
    response = requests.get(url)
    html = response.text

    return findall(r'<span class="repo" title="(.+?)"', html)


@cache
def get_pins_from_html_stream(url: str):
    response = requests.get(url, stream=True)

    repos = []

    for line in response.iter_lines(decode_unicode=True):

        if '<span class="repo" title="' in line:
            repos += findall(r'<span class="repo" title="(.+?)"', line)

        if len(repos) >= 1 and '</ol>' in line:
            break

    return repos


@cache
def get_pins_from_api(user: str):
    response = requests.get(f'https://gh-pinned-repos.egoist.dev/?username={user}')
    json = response.json()

    return [*map(lambda x: x['repo'], json)]