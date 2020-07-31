class Logs(object):

    @staticmethod
    def info(mensagem : str):
        print(f'[INFO] {mensagem}')

    @staticmethod
    def error(mensagem : str):
        print(f'[ERROR] {mensagem}')

    @staticmethod
    def warning(mensagem : str):
        print(f'[WARNING] {mensagem}')