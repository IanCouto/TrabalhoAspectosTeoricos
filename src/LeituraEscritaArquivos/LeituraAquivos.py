from src.Utils.Logs import Logs

caminho = '../../input/'


class LeituraArquivos(object):
    @staticmethod
    def ler(arquivo: str):
        try:
            file = open(caminho + arquivo, 'r')
            read_data = file.readlines()
            file.close()
            return read_data
        except IOError:
            Logs.error(f'Arquivo \"{arquivo}\" não encontrado!')
            return False
