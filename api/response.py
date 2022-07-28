#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Any


errors = {
    0: 'success',
    1: 'common error',
    200: 'http success',
    400: 'client error',
    500: 'server error',
}


def error(code: int, message: str = None, result: Any = None) -> dict:
    message = message or errors[code]
    return {
        "code": code,
        "message": message,
        "result": result,
    }


def success(result: Any = None) -> dict:
    return error(code=0, result=result)
