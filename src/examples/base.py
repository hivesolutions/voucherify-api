#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import voucherify


def get_api():
    return voucherify.API(
        client_id=appier.conf("VOUCHERIFY_ID"),
        client_secret=appier.conf("VOUCHERIFY_SECRET"),
    )
