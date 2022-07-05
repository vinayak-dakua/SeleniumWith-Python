import inspect
import logging

class LogGen:

    @staticmethod
    def loggen():
        # logging.basicConfig(filename='C:\\Users\\vinay\\PycharmProjects\\PythonWithSelenium\\Logs\\automation.log',
        #                     format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S %p' )
        #
        # logger = logging.getLogger()
        # logger.setLevel(logging.INFO)
        # return logger

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('C:\\Users\\vinay\\PycharmProjects\\PythonWithSelenium\\Logs\\automation.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.INFO)
        return logger