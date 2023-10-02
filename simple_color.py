class SimpleColor:
    COLORS = {
        'reset': '\033[0m',
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'gray': '\033[90m',
        'light_red': '\033[91m',
        'light_green': '\033[92m',
        'light_yellow': '\033[93m',
        'light_blue': '\033[94m',
        'light_purple': '\033[95m',
        'light_cyan': '\033[96m',
        'pink': '\033[95m',
        'orange': '\033[93m',
        'teal': '\033[96m',
        'dark_gray': '\033[30;1m',
        'dark_red': '\033[31;1m',
        'dark_green': '\033[32;1m',
        'dark_yellow': '\033[33;1m',
        'dark_blue': '\033[34;1m',
        'dark_purple': '\033[35;1m',
        'dark_cyan': '\033[36;1m',
        'light_gray': '\033[37;1m',
        'bold_white': '\033[97m',
        'bg_black': '\033[40m',
        'bg_red': '\033[41m',
        'bg_green': '\033[42m',
        'bg_yellow': '\033[43m',
        'bg_blue': '\033[44m',
        'bg_purple': '\033[45m',
        'bg_cyan': '\033[46m',
        'bg_white': '\033[47m',
        'bg_light_gray': '\033[100m',
        'bg_dark_gray': '\033[100;1m',
        'bg_light_red': '\033[101m',
        'bg_light_green': '\033[102m',
        'bg_light_yellow': '\033[103m',
        'bg_light_blue': '\033[104m',
        'bg_light_purple': '\033[105m',
        'bg_light_cyan': '\033[106m',
        'bg_bold_white': '\033[107m',
    }

    instareset = False

    @staticmethod
    def colorize(text, text_color, bg_color=None):
        text_color_code = SimpleColor.COLORS.get(text_color.lower())
        bg_color_code = SimpleColor.COLORS.get(bg_color.lower()) if bg_color else ""

        if text_color_code:
            return f"{text_color_code}{bg_color_code}{text}" + (SimpleColor.COLORS['reset'] if SimpleColor.instareset else "")
        else:
            return text

    @staticmethod
    def hex_colorize(text, hex_color, bg_color=None):
        if not hex_color.startswith("#") or len(hex_color) != 7:
            return text

        text_color_code = f'\033[38;2;{int(hex_color[1:3], 16)};{int(hex_color[3:5], 16)};{int(hex_color[5:], 16)}m'
        bg_color_code = SimpleColor.COLORS.get(bg_color.lower()) if bg_color else ""

        return f"{text_color_code}{bg_color_code}{text}" + (SimpleColor.COLORS['reset'] if SimpleColor.instareset else "")

    @staticmethod
    def clear_terminal():
        print('\033c', end='')  # Clear the terminal screen

# Example usage:
if __name__ == "__main__":
    text = "Hello, VisualSynced!"

    # Using custom text color and background color
    colored_text = SimpleColor.colorize(text, 'light_blue', 'bg_red')
    print(colored_text)

    # Using custom hex text color and background color
    colored_text_hex = SimpleColor.hex_colorize(text, '#FFA500', 'bg_green')  # Orange text on green background
    print(colored_text_hex)

    # Clear terminal
    SimpleColor.clear_terminal()
