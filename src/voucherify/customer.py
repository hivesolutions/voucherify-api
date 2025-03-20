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

    def get_customer(self, customer_id):
        url = self.base_url + "customers/%s" % customer_id
        contents = self.get(url)
        return contents

    def update_customer(self, customer_id, payload):
        url = self.base_url + "customers/%s" % customer_id
        contents = self.put(url, data_j=payload)
        return contents
