# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.error import Error
from swagger_server.models.glstring import Glstring
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_act_get(self):
        """
        Test case for act_get

        
        """
        query_string = [('glstring', 'glstring_example'),
                        ('dbversion', 'dbversion_example'),
                        ('neo4j_url', 'neo4j_url_example'),
                        ('user', 'user_example'),
                        ('password', 'password_example'),
                        ('verbose', true)]
        response = self.client.open('/act',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
