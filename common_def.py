# -*- coding: utf-8 -*-

def str_to_digital_type(value: int | float | str) -> int | float:

    """
    将输入值转换为数字类型（int 或 float）
    """

    error_text = "please enter a number"

    if isinstance(value, (int, float)):
        return value
    if isinstance(value, str):
        for cast in (int, float):
            try:
                return cast(value)
            except ValueError:
                continue
        raise TypeError(error_text)
    else:
        raise TypeError(error_text)
