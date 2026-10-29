import io
from contextlib import redirect_stdout

# Customer classes:
from classes.colors import Color
from classes.logger import Logger

# Instantiations:

color = Color()
logger = Logger()

################

def full_test():
    tests = 0
    successes = 0
    failures = 0

    try:
        tests += 1
        print(logger.test("[1]Testing Logger class instantiates..."))
        assert isinstance(logger, Logger), "Logger did not initialize as a Logger instance."

        print(logger.test("[1]Testing Logger's INFO terminal output..."))
        message = "info test."
        output_stream = io.StringIO()
        with redirect_stdout(output_stream):
            print(logger.info(message))
        output = output_stream.getvalue()
        print(output, end="")
        assert "INFO:" in output, "INFO label did not populate."
        assert message in output, "INFO did not preserve the supplied message."
        assert output.count(message) == 1, "INFO duplicated the message."
        assert output.count("\n") == 1, "INFO did not produce exactly one output line."

        print(logger.test("[1]Testing Logger's WARNING terminal output..."))
        message = "warning test."
        output_stream = io.StringIO()
        with redirect_stdout(output_stream):
            print(logger.warning(message))
        output = output_stream.getvalue()
        print(output, end="")
        assert "WARNING:" in output, "WARNING label did not populate."
        assert message in output, "WARNING did not preserve the supplied message."
        assert output.count(message) == 1, "WARNING duplicated the message."
        assert output.count("\n") == 1, "WARNING did not produce exactly one output line."

        print(logger.test("[1]Testing Logger's ERROR terminal output..."))
        message = "error test."
        output_stream = io.StringIO()
        with redirect_stdout(output_stream):
            print(logger.error(message))
        output = output_stream.getvalue()
        print(output, end="")
        assert "ERROR:" in output, "ERROR label did not populate."
        assert message in output, "ERROR did not preserve the supplied message."
        assert output.count(message) == 1, "ERROR duplicated the message."
        assert output.count("\n") == 1, "ERROR did not produce exactly one output line."

        print(logger.test("[1]Testing Logger's TEST terminal output..."))
        message = "test test."
        output_stream = io.StringIO()
        with redirect_stdout(output_stream):
            print(logger.test(message))
        output = output_stream.getvalue()
        print(output, end="")
        assert "TEST:" in output, "TEST label did not populate."
        assert message in output, "TEST did not preserve the supplied message."
        assert output.count(message) == 1, "TEST duplicated the message."
        assert output.count("\n") == 1, "TEST did not produce exactly one output line."

        print(logger.test("[1]Testing Color class is instantiating."))
        assert isinstance(color, Color), "Color did not initialize as a Color instance."

        print(logger.test("[1]Testing Color's BLACK terminal output and RESET taking effect..."))
        message = "black test."
        output_stream = io.StringIO()
        with redirect_stdout(output_stream):
            print(color.black(message))
        output = output_stream.getvalue()
        print(output, end="")
        assert output.startswith("\033[30m"), "BLACK color code did not start the output."
        assert output.endswith("\033[0m\n"), "RESET code did not end the output."
        assert message in output, "Color did not preserve the supplied message."
        assert output.count(message) == 1, "Color duplicated the supplied message."

        print(logger.test("[1]Testing Color's RED terminal output and RESET taking effect..."))
        message = "red test."
        output_stream = io.StringIO()
        with redirect_stdout(output_stream):
            print(color.red(message))
        output = output_stream.getvalue()
        print(output, end="")
        assert output.startswith("\033[31m"), "RED color code did not start the output."
        assert output.endswith("\033[0m\n"), "RESET code did not end the output."
        assert message in output, "Color did not preserve the supplied message."
        assert output.count(message) == 1, "Color duplicated the supplied message."

        print(logger.test("[1]Testing Color's GREEN terminal output and RESET taking effect..."))
        message = "green test."
        output_stream = io.StringIO()
        with redirect_stdout(output_stream):
            print(color.green(message))
        output = output_stream.getvalue()
        print(output, end="")
        assert output.startswith("\033[32m"), "GREEN color code did not start the output."
        assert output.endswith("\033[0m\n"), "RESET code did not end the output."
        assert message in output, "Color did not preserve the supplied message."
        assert output.count(message) == 1, "Color duplicated the supplied message."

        print(logger.test("[1]Testing Color's YELLOW terminal output and RESET taking effect..."))
        message = "yellow test."
        output_stream = io.StringIO()
        with redirect_stdout(output_stream):
            print(color.yellow(message))
        output = output_stream.getvalue()
        print(output, end="")
        assert output.startswith("\033[33m"), "YELLOW color code did not start the output."
        assert output.endswith("\033[0m\n"), "RESET code did not end the output."
        assert message in output, "Color did not preserve the supplied message."
        assert output.count(message) == 1, "Color duplicated the supplied message."

        print(logger.test("[1]Testing Color's BLUE terminal output and RESET taking effect..."))
        message = "blue test."
        output_stream = io.StringIO()
        with redirect_stdout(output_stream):
            print(color.blue(message))
        output = output_stream.getvalue()
        print(output, end="")
        assert output.startswith("\033[34m"), "BLUE color code did not start the output."
        assert output.endswith("\033[0m\n"), "RESET code did not end the output."
        assert message in output, "Color did not preserve the supplied message."
        assert output.count(message) == 1, "Color duplicated the supplied message."

        print(logger.test("[1]Testing Color's PURPLE terminal output and RESET taking effect..."))
        message = "purple test."
        output_stream = io.StringIO()
        with redirect_stdout(output_stream):
            print(color.purple(message))
        output = output_stream.getvalue()
        print(output, end="")
        assert output.startswith("\033[35m"), "PURPLE color code did not start the output."
        assert output.endswith("\033[0m\n"), "RESET code did not end the output."
        assert message in output, "Color did not preserve the supplied message."
        assert output.count(message) == 1, "Color duplicated the supplied message."

        print(logger.test("[1]Testing Color's CYAN terminal output and RESET taking effect..."))
        message = "cyan test."
        output_stream = io.StringIO()
        with redirect_stdout(output_stream):
            print(color.cyan(message))
        output = output_stream.getvalue()
        print(output, end="")
        assert output.startswith("\033[36m"), "CYAN color code did not start the output."
        assert output.endswith("\033[0m\n"), "RESET code did not end the output."
        assert message in output, "Color did not preserve the supplied message."
        assert output.count(message) == 1, "Color duplicated the supplied message."

        print(logger.test("[1]Testing Color's WHITE terminal output and RESET taking effect..."))
        message = "white test."
        output_stream = io.StringIO()
        with redirect_stdout(output_stream):
            print(color.white(message))
        output = output_stream.getvalue()
        print(output, end="")
        assert output.startswith("\033[37m"), "WHITE color code did not start the output."
        assert output.endswith("\033[0m\n"), "RESET code did not end the output."
        assert message in output, "Color did not preserve the supplied message."
        assert output.count(message) == 1, "Color duplicated the supplied message."

        print(logger.test("[1]Testing Logger's INFO terminal output utilizing BLUE..."))
        message = "info blue test."
        output_stream = io.StringIO()
        with redirect_stdout(output_stream):
            print(logger.info(message))
        output = output_stream.getvalue()
        print(output, end="")
        assert output.startswith("\033[34m"), "INFO did not apply BLUE."
        assert "INFO:" in output, "INFO label did not populate."
        assert message in output, "INFO did not preserve the supplied message."
        assert output.endswith("\033[0m\n"), "INFO did not reset the terminal color."

        print(logger.test("[1]Testing Logger's WARNING terminal output utilizing YELLOW..."))
        message = "warning yellow test."
        output_stream = io.StringIO()
        with redirect_stdout(output_stream):
            print(logger.warning(message))
        output = output_stream.getvalue()
        print(output, end="")
        assert output.startswith("\033[33m"), "WARNING did not apply YELLOW."
        assert "WARNING:" in output, "WARNING label did not populate."
        assert message in output, "WARNING did not preserve the supplied message."
        assert output.endswith("\033[0m\n"), "WARNING did not reset the terminal color."

        print(logger.test("[1]Testing Logger's ERROR terminal output utilizing RED..."))
        message = "error red test."
        output_stream = io.StringIO()
        with redirect_stdout(output_stream):
            print(logger.error(message))
        output = output_stream.getvalue()
        print(output, end="")
        assert output.startswith("\033[31m"), "ERROR did not apply RED."
        assert "ERROR:" in output, "ERROR label did not populate."
        assert message in output, "ERROR did not preserve the supplied message."
        assert output.endswith("\033[0m\n"), "ERROR did not reset the terminal color."

        print(logger.test("[1]Testing Logger's TEST terminal output utilizing CYAN..."))
        message = "test cyan test."
        output_stream = io.StringIO()
        with redirect_stdout(output_stream):
            print(logger.test(message))
        output = output_stream.getvalue()
        print(output, end="")
        assert output.startswith("\033[36m"), "TEST did not apply CYAN."
        assert "TEST:" in output, "TEST label did not populate."
        assert message in output, "TEST did not preserve the supplied message."
        assert output.endswith("\033[0m\n"), "TEST did not reset the terminal color."

        successes += 1
        print(color.green("Version 0.0.1 text coloring and logging is online."))
    except Exception as e:
        failures += 1
        print(logger.error(e))
        print(color.red("Version 0.0.1 text coloring and logging is a failure"))

    if failures > 0:
        print(color.red(f"{failures} failures detected, please fix."))
    else:
        print(color.green(f"Things are operational with {successes}/{tests} tests passed."))
