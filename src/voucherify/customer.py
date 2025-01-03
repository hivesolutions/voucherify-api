#!/usr/bin/python
# -*- coding: utf-8 -*-


class CustomerAPI(object):

    def list_customers(self, *args, **kwargs):
        url = self.base_url + "customers"
        contents = self.get(url, **kwargs)
        return contents

    def create_customer(self, payload):
        url = self.base_url + "customers"
        contents = self.post(url, data_j=payload)
        return contents
