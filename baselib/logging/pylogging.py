#!/usr/bin/env python
# -*-coding:utf-8 -*-
import logging
import os
import logging.config

def setup_logging():
    configfile = os.path.join(os.path.dirname(__file__), 'logging.ini')
    logging.config.fileConfig(configfile)
    logger = logging.getLogger(__file__)
    logger.debug('load logging module successfully!')


# if __name__ == "__main__":
#     setup_logging()
#     logger = logging.getLogger('aquapaas')
#     logger.debug("msg")
