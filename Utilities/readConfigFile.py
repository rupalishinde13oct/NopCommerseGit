import configparser

config = configparser.RawConfigParser()

config.read("D:\\Rupali Prathamesh Pandit\\NonCommerse\\Configuration\\config.ini")

class ReadConfig:

    @staticmethod
    def getUrl():
        url = config.get('common info' , 'Url')
        return url

    @staticmethod
    def getEmail():
        email = config.get('common info', 'Email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('common info', 'Password')
        return password


