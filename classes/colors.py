class Color():
#-------------
# Color Constants
#-------------

    def __init__(self):
        self.BLACK = "\033[30m"
        self.RED = "\033[31m"
        self.GREEN = "\033[32m"
        self.YELLOW = "\033[33m"
        self.BLUE = "\033[34m"
        self.PURPLE = "\033[35m"
        self.CYAN = "\033[36m"
        self.WHITE = "\033[37m"

        self.RESET = "\033[0m"

#-------------
# Color Helpers
#-------------

    def black(self, str):
        return f"{self.BLACK}{str}{self.RESET}"

    def red(self, str):
        return f"{self.RED}{str}{self.RESET}"

    def green(self, str):
        return f"{self.GREEN}{str}{self.RESET}"

    def yellow(self, str):
        return f"{self.YELLOW}{str}{self.RESET}"

    def blue(self, str):
        return f"{self.BLUE}{str}{self.RESET}"

    def purple(self, str):
        return f"{self.PURPLE}{str}{self.RESET}"

    def cyan(self, str):
        return f"{self.CYAN}{str}{self.RESET}"

    def white(self, str):
        return f"{self.WHITE}{str}{self.RESET}"