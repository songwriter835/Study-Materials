# -*- coding: utf-8 -*-

def str_to_digital_type(str_):
    if  isinstance(str_, (int, float)):
        return str_
    for cast in (int, float):
        try:
            return cast(str_)
        except ValueError:
            pass
    raise TypeError("please enter a number")
