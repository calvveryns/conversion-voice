import configparser


# A method that receives a configuration file with tokens as input
def get_config(filename):
    config = configparser.ConfigParser()
    try:
        config.read(filename)
        return config['Telegram']['BOT_TOKEN']
    except FileNotFoundError:
        print(f'File {filename} not found!')
