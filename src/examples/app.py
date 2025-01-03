#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import base


class SimpleApp(appier.APIApp):

    def __init__(self, *args, **kwargs):
        appier.APIApp.__init__(self, name="mb", *args, **kwargs)
        self.api = base.get_api()
        self.api.bind("paid", self.on_paid)


if __name__ == "__main__":
    app = SimpleApp()
    app.serve()
else:
    __path__ = []
