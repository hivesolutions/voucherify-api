#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import base


class SimpleApp(appier.APIApp):

    def __init__(self, *args, **kwargs):
        appier.APIApp.__init__(self, name="mb", *args, **kwargs)
        self.api = base.get_api()

    @appier.route("/customers", "GET")
    def customers(self):
        return self.api.list_customers()


if __name__ == "__main__":
    app = SimpleApp()
    app.serve()
else:
    __path__ = []
