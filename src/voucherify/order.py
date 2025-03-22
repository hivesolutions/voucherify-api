#!/usr/bin/python
# -*- coding: utf-8 -*-


class OrderAPI(object):

    def list_orders(self, *args, **kwargs):
        url = self.base_url + "orders"
        contents = self.get(url, **kwargs)
        return contents

    def create_order(self, payload):
        url = self.base_url + "orders"
        contents = self.post(url, data_j=payload)
        return contents

    def get_orders(self, order_id):
        url = self.base_url + "orders/%s" % order_id
        contents = self.get(url)
        return contents

    def update_order(self, order_id, payload):
        url = self.base_url + "orders/%s" % order_id
        contents = self.put(url, data_j=payload)
        return contents
