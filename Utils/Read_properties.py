import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\configs.ini')

class Read_Configs:

    @staticmethod
    def get_application_url():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def get_username():
        username = config.get('common info', 'customerName')
        return username

    @staticmethod
    def get_browser():
        browser = config.get('common info', 'browser')
        return browser

    @staticmethod
    def get_implicit_wait():
        implicit_wait = config.get('common info', 'implicit_wait')
        return implicit_wait

    @staticmethod
    def get_explicit_wait():
        explicit_wait = config.get('common info', 'explicit_wait')
        return explicit_wait
