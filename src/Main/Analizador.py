from src.Utils.Logs import Logs
from src.Main.Tags import Tags


class Analizador(object):
    __texto = ''
    __resultado = []

    def set_texto(self, texto: str):
        self.__texto = texto

    def get_texto(self):
        return self.__texto

    def get_resultado(self):
        return self.__resultado

    # Retorna True para analize realizada com sucesso ou False para o contrario
    def analizar(self, tags: Tags):
        if self.__texto == '':
            Logs.error('Não a texto à analizar!')
            return False
        # Método para analizar texto (a fazer)
        return True
