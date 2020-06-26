__all__ = (
    'WebpackError',
    'WebpackLoaderBadStatsError',
    'WebpackLoaderTimeoutError',
    'WebpackBundleLookupError'
)


class BaseWebpackLoaderException(Exception):
    """
    Base exception for django-create-react-app.
    """


class WebpackError(BaseWebpackLoaderException):
    """
    General webpack loader error.
    """


class WebpackLoaderBadStatsError(BaseWebpackLoaderException):
    """
    The Build has not accept manifest file.
    """


class WebpackLoaderTimeoutError(BaseWebpackLoaderException):
    """
    The bundle took too long to compile.
    """


class WebpackBundleLookupError(BaseWebpackLoaderException):
    """
    The bundle name was invalid.
    """
