#!/usr/bin/python
# -*- coding: utf-8 -*-


class ValidationAPI(object):

    def create_validation(self, payload):
        url = self.base_url + "validations"
        contents = self.post(url, data_j=payload)
        return contents
