import logging

class Logging:
    @staticmethod
    def loggen():

        loger = logging.getLogger()

        file = logging.FileHandler("D:\\Rupali Prathamesh Pandit\\NonCommerse\\Logs\\NonCommerseLogs.log")
        format = logging.Formatter(" %(asctime)s : %(levelno)s : %(message)s")
        file.setFormatter(format)

        loger.addHandler(file)
        loger.setLevel(logging.INFO)
        return loger
