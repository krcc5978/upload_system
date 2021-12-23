import configparser


class SystemConfig:

    def __init__(self, log, config_path):
        self.config = configparser.ConfigParser()
        self.config.read(config_path, 'UTF-8')
        self.log = log

    def get_config(self, section, option=None):

        if not self.config.has_section(section):
            self.log.error(f'>> {section} is not found')
            return None

        if option is None:
            return True

        if self.config.has_option(section, option):
            return self.config.get(section, option)
        else:
            self.log.error(f'>> {option} is not found')
            return None
