

def update_config(config_model, *args):
    config_model.config.set('SERVER', 'ip', args[0])
    config_model.config.set('SERVER', 'pc_name', args[1])
    config_model.config.set('SERVER', 'share_folder', args[2])
    config_model.config.set('SERVER', 'directory', args[3])
    config_model.config.set('USER', 'ID', args[4])
    config_model.config.set('USER', 'PASS', args[5])
    config_model.config.write(open(config_model.config_path, 'w', encoding='UTF-8'))