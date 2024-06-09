import configparser

# parse data inside config object
config = configparser.RawConfigParser()
# load data
config.read(".\\configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def get_base_url():
        url = config.get('API', 'base_url')
        return url

    @staticmethod
    def get_auth_token():
        auth_token = config.get('API', 'auth_token')
        return auth_token

    # @staticmethod
    # def get_header_content_type():
    #     content_type = config.get('Headers', 'content_type')
    #     return content_type

    @staticmethod
    def get_header_content_type():
        # Return a dictionary instead of a string
        return {
            "Content-Type": "application/json"
        }
