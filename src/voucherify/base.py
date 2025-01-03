#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import customer
from . import validation

BASE_URL = "https://api.voucherify.io/v1/"
""" The default base URL to be used for a production
based environment, should be used carefully """


class API(appier.API, customer.CustomerAPI, validation.ValidationAPI):

    def __init__(self, *args, **kwargs):
        appier.API.__init__(self, *args, **kwargs)
        self.client_id = appier.conf("VOUCHERIFY_ID", None)
        self.client_secret = appier.conf("VOUCHERIFY_SECRET", None)
        self.client_id = kwargs.get("client_id", self.client_id)
        self.client_secret = kwargs.get("client_secret", self.client_secret)
        self.base_url = kwargs.get("base_url", BASE_URL)

    def build(
        self,
        method,
        url,
        data=None,
        data_j=None,
        data_m=None,
        headers=None,
        params=None,
        mime=None,
        kwargs=None,
    ):
        appier.API.build(self, method, url, headers, kwargs)
        if self.client_id:
            headers["X-App-Id"] = self.client_id
        if self.client_secret:
            headers["X-App-Token"] = self.client_secret
