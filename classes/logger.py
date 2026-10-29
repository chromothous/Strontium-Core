from classes.colors import Color

# Instantiations
color = Color()

class Logger():

    def info(self, message):
        return color.blue(f"INFO: {message}")

    def warning(self, message):
        return color.yellow(f"WARNING: {message}")

    def error(self, message):
        return color.red(f"ERROR: {message}")

    def test(self, message):
        return color.cyan(f"TEST: {message}")