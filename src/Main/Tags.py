from src.Utils.Logs import Logs


class Tags(object):
    __tags = {}

    def adicionar_tag(self, nometag: str, tag: str):
        if self.valida_tag(nometag, tag):
            self.__tags[nometag] = tag
            Logs.info(f'A tag {nometag} foi inserida!')

    def remover_tag(self, nometag):
        if nometag in self.__tags:
            del self.__tags[nometag]

    def get_tag(self, nometag):
        if nometag in self.__tags:
            return self.__tags[nometag]
        else:
            return ''

    def get_todas_tags(self):
        return self.__tags

    def valida_tag(self, nometag: str, tag: str):
        # Tag já existente
        if nometag in self.__tags:
            Logs.error(f'A tag {nometag} já foi inserida!')
            return False

        # Método para validar a tag (a fazer)
        return True
