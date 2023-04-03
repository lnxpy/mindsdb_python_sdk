
from mindsdb_sdk.__about__ import __package_name__ as name, __version__

from .server import Server


def connect(url: str = None, email: str = None, password: str = None, is_managed: bool = False) -> Server:
    """
    Create connection to mindsdb server

    :param url: url to mindsdb server
    :param email: user email to login (for cloud version)
    :param password: user password to login (for cloud version)
    :param is_managed: whether or not the URL points to a managed instance
    :return: Server object

    Examples
    --------

    >>> import mindsdb_sdk

    Connect to local server

    >>> server = mindsdb_sdk.connect()
    >>> server = mindsdb_sdk.connect('http://127.0.0.1:47334')

    Connect to cloud server

    >>> server = mindsdb_sdk.connect(email='a@b.com', password='-')
    >>> server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email='a@b.com', password='-')

    Connect to MindsDB pro

    >>> server = mindsdb_sdk.connect('http://<YOUR_INSTANCE_IP>', email='a@b.com', password='-', is_managed=True)

    """
    if url is None:
        if email is not None:
            # default is cloud
            url = 'https://cloud.mindsdb.com'
        else:
            # is local
            url = 'http://127.0.0.1:47334'

    return Server(url=url, email=email, password=password, is_managed=is_managed)
