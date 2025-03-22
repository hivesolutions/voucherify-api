#!/usr/bin/python
# -*- coding: utf-8 -*-


class RedemptionAPI(object):

    def create_redemption(self, payload):
        url = self.base_url + "redemptions"
        contents = self.post(url, data_j=payload)
        return contents
