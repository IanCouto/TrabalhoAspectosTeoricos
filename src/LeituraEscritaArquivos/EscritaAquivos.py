from src.Utils.Logs import Logs

caminho = '../../output/'


class EscritaArquivos(object):
    __file = None
    __escrevendo = False

    # Método de escrita de instância para multiplas escritas em mesmo arquivo
    def escrever(self, arquivo: str, conteudo: str):
        try:
            if self.__file is None:
                self.__file = open(caminho + arquivo, 'w')
            self.__file.write(conteudo)
            self.__escrevendo = True
        except IOError:
            Logs.error('Erro ao escrever arquivo!')

    def fechar_arquivo(self):
        if self.__escrevendo:
            self.__file.close()

    # Método de escrita estático para escritas individuais (sem reescrita ou adição de escrita)
    @staticmethod
    def escrever_static(arquivo: str, conteudo: str):
        try:
            file = open(caminho + arquivo, 'w')
            file.write(conteudo)
            file.close()
            Logs.info(f'O arquivo {arquivo} foi salvo!')
        except IOError:
            Logs.error('Erro ao escrever arquivo!')
