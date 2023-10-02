#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SimpleColor"""

import typing

COLORS: typing.Final[dict[str, str]] = {
    "reset": "\33[0m",
    "black": "\33[30m",
    "red": "\33[31m",
    "green": "\33[32m",
    "yellow": "\33[33m",
    "blue": "\33[34m",
    "purple": "\33[35m",
    "cyan": "\33[36m",
    "white": "\33[37m",
    "gray": "\33[90m",
    "light_red": "\33[91m",
    "light_green": "\33[92m",
    "light_yellow": "\33[93m",
    "light_blue": "\33[94m",
    "light_purple": "\33[95m",
    "light_cyan": "\33[96m",
    "pink": "\33[95m",
    "orange": "\33[93m",
    "teal": "\33[96m",
    "dark_gray": "\33[30;1m",
    "dark_red": "\33[31;1m",
    "dark_green": "\33[32;1m",
    "dark_yellow": "\33[33;1m",
    "dark_blue": "\33[34;1m",
    "dark_purple": "\33[35;1m",
    "dark_cyan": "\33[36;1m",
    "light_gray": "\33[37;1m",
    "bold_white": "\33[97m",
    "bg_black": "\33[40m",
    "bg_red": "\33[41m",
    "bg_green": "\33[42m",
    "bg_yellow": "\33[43m",
    "bg_blue": "\33[44m",
    "bg_purple": "\33[45m",
    "bg_cyan": "\33[46m",
    "bg_white": "\33[47m",
    "bg_light_gray": "\33[100m",
    "bg_dark_gray": "\33[100;1m",
    "bg_light_red": "\33[101m",
    "bg_light_green": "\33[102m",
    "bg_light_yellow": "\33[103m",
    "bg_light_blue": "\33[104m",
    "bg_light_purple": "\33[105m",
    "bg_light_cyan": "\33[106m",
    "bg_bold_white": "\33[107m",
}


def colorize(
    text: str,
    text_color: str,
    bg_color: typing.Optional[str] = None,
    reset: bool = False,
) -> str:
    text_color_code: typing.Optional[str] = COLORS.get(text_color.lower())
    bg_color_code: typing.Optional[str] = (
        COLORS.get(bg_color.lower()) if bg_color else ""
    )

    return (
        f"{text_color_code}{bg_color_code}{text}{COLORS['reset'] if reset else ''}"
        if text_color_code
        else text
    )


def hex_colorize(
    text: str,
    hex_color: str,
    bg_color: typing.Optional[str] = None,
    reset: bool = False,
) -> str:
    if not hex_color.startswith("#") or len(hex_color) != 7:
        return text

    text_color_code: str = f"\33[38;2;{int(hex_color[1:3], 16)};{int(hex_color[3:5], 16)};{int(hex_color[5:], 16)}m"
    bg_color_code: str = COLORS.get(bg_color.lower(), "") if bg_color else ""

    return f"{text_color_code}{bg_color_code}{text}{COLORS['reset'] if reset else ''}"


@staticmethod
def clear_terminal():
    print("\33c", end="")  # Clear the terminal screen


