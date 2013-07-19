"""
This configuration file loads environment's specific config settings for the application.
It takes precedence over the config located in the boilerplate package.
"""

import os

if "SERVER_SOFTWARE" in os.environ:
    if os.environ['SERVER_SOFTWARE'].startswith('Dev'):
        from config.localhost import config as environment_config

    elif os.environ['SERVER_SOFTWARE'].startswith('Google'):
        from config.production import config as environment_config
else:
    from config.testing import config as environment_config

from config.base import config
config.update(environment_config)
