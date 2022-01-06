import configparser


class ConfigSystemModel:

    def __init__(self, config_path):
        self.config_path = config_path

        self.config = configparser.ConfigParser()
        self.config.read(self.config_path, 'UTF-8')

        self.ip = self.config['SERVER']['IP']
        self.pc_name = self.config['SERVER']['PC_NAME']
        self.share_folder = self.config['SERVER']['SHARE_FOLDER']
        self.directory = self.config['SERVER']['DIRECTORY']
        self.login_id = self.config['USER']['ID']
        self.login_pass = self.config['USER']['PASS']
