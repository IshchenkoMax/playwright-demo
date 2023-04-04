from urllib import parse
from urllib.parse import urlparse


def url_parser_query(url_string: str, query_name: str):
    try:
        query = dict(parse.parse_qsl(urlparse(url_string).query))
        if query[query_name]:
            return query[query_name]
    except Exception:
        raise Exception(f'no query in the url - {query_name}')
