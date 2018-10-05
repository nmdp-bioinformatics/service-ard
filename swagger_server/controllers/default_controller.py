import connexion
from swagger_server.models.error import Error
from swagger_server.models.glstring import Glstring
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import pyard
from pyard import ARD
import pandas as pd
import logging
import io

ard_dict = {}


def ard_get(glstring, ard_type="G", dbversion='Latest', verbose=None):
    """
    act_get
    Get HLA and GFE from consensus sequence or GFE notation
    :param glstring: Valid glstring
    :type glstring: str
    :param dbversion: URL for the neo4j graph
    :type dbversion: str
    :param neo4j_url: URL for the neo4j graph
    :type neo4j_url: str
    :param user: Username for the neo4j graph
    :type user: str
    :param password: Password for the neo4j graph
    :type password: str
    :param verbose: Flag for running service in verbose
    :type verbose: bool

    :rtype: Glstring
    """
    global ard_dict

    dbversion = "".join(dbversion.split("."))
    log_capture_string = io.StringIO()
    logger = logging.getLogger('')
    logging.basicConfig(datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging.INFO)

    # create console handler and set level to debug
    ch = logging.StreamHandler(log_capture_string)
    formatter = logging.Formatter('%(asctime)s - %(name)-35s - %(levelname)-5s - %(funcName)s %(lineno)d: - %(message)s')
    ch.setFormatter(formatter)
    ch.setLevel(logging.INFO)
    logger.addHandler(ch)

    if dbversion not in ard_dict:
        try:
            ard = ARD(dbversion=dbversion, verbose=True)
        except:
            log_contents = log_capture_string.getvalue()
            return Error(message="An error loading ARD object",
                         log=log_contents.split("\n"),
                         version=pyard.__version__), 404
        ard_dict.update({dbversion: ard})
    else:
        ard = ard_dict[dbversion]

    try:
        glard = ard.redux_gl(glstring, ard_type)
    except:
        log_contents = log_capture_string.getvalue()
        return Error(message="An error occured during the ARD reduction",
                     log=log_contents.split("\n"),
                     version=pyard.__version__), 404

    return glard
