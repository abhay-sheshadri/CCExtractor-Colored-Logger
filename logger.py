import coloredlogs
import logging
# Basic format
format = "%(asctime)s,%(msecs)03d %(name)s[%(process)d] %(levelname)s %(message)s"

coloredlogs.DEFAULT_FIELD_STYLES = {'asctime': {'color': 'green'}, 'msecs': {'color': 'magenta'}, 'levelname': {'color': 'red', 'bold': True}, 'name': {'color': 'cyan'}, 'programname': {'color': 'cyan'}}

# Colored Logging
logger = logging.getLogger(__name__ + ".info")
coloredlogs.install(fmt=format,level="INFO", logger=logger)
logger.setLevel(logging.INFO)

# Logging DEBUG to files
file_logger = logging.getLogger(__name__ + ".debug")
file_logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(format)
file_handler = logging.FileHandler("sample.log")
file_handler.setFormatter(formatter)

file_logger.addHandler(file_handler)

def main():
    # STDOUT
    logger.info("Welcome to the info level")
    logger.info("This should be in color")

    # sample.log
    file_logger.debug("This is the debug level")
    file_logger.debug("This is in a file")

if __name__ == "__main__":
    main()
