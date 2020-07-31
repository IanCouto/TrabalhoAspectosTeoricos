# Arquivo principal (Main)
from src.Utils.Logs import Logs
from src.Main.Tags import Tags
from src.Main.Analizador import Analizador
from src.LeituraEscritaArquivos.LeituraAquivos import LeituraArquivos
from src.LeituraEscritaArquivos.EscritaAquivos import EscritaArquivos

tags = Tags()
analizador = Analizador()
escrever_resul = EscritaArquivos()
arq_saida = ''

while True:
    entrada = input()
    if entrada.startswith(':d') or entrada.startswith(':D'):  # Realiza a divisão em tags da string do arquivo informado
        nome_arquivo = entrada[2:]  # remove a opção :q
        nome_arquivo = nome_arquivo.strip()  # remove espaços iniciais e finais
        if ' ' in nome_arquivo:
            Logs.error('Nome de arquivo não pode conter espaços!')
        else:
            if nome_arquivo:
                arquivo_texto = LeituraArquivos.ler(nome_arquivo)
                if arquivo_texto:
                    analizador.set_texto(arquivo_texto)
                    if analizador.analizar(tags):
                        # caso não tiver arquivo para saida, imprimir em tela
                        if arq_saida:
                            escrever_resul.escrever(arq_saida, ' '.join(analizador.get_resultado()))
                            Logs.info('Resultado salvo em arquivo!')
                        else:
                            print(analizador.get_resultado())
            else:
                Logs.error('Arquivo não especificado!')

    elif entrada.startswith(':c') or entrada.startswith(':C'):  # Carrega um arquivo com definições de tags
        nome_arquivo = entrada[2:]  # remove a opção :c
        nome_arquivo = nome_arquivo.strip()  # remove espaços iniciais e finais
        if ' ' in nome_arquivo:
            Logs.error('Nome de arquivo não pode conter espaços!')
        else:
            if nome_arquivo:
                arquivo_tags = LeituraArquivos.ler(nome_arquivo)
                if arquivo_tags:
                    for linha in arquivo_tags:
                        if ': ' in linha:
                            tag = linha.split(': ', 1)  # divide a tags em nome_tag (tag[0]) e a tag em si (tag[1])
                            tag = [i.strip() for i in tag]  # remove possiveis espaços iniciais e finais
                            tags.adicionar_tag(tag[0].upper(), tag[1])
                        else:
                            Logs.error('Formato inválido de tag!')
                    Logs.info('Todas as tags foram lidas!')
            else:
                Logs.error('Arquivo não especificado!')

    elif entrada.startswith(':o') or entrada.startswith(':O'):  # Especifica o caminho do arquivo de saída para a divisão em tags
        nome_arquivo = entrada[2:]  # remove a opção :o
        nome_arquivo = nome_arquivo.strip()  # remove espaços iniciais e finais
        if ' ' in nome_arquivo:
            Logs.error('Nome de arquivo não pode conter espaços!')
        else:
            if nome_arquivo:
                arq_saida = nome_arquivo
                Logs.info('Arquivo de saída especificado!')
            else:
                Logs.error('Arquivo de saida não fornecido!')

    elif entrada.startswith(':p') or entrada.startswith(':P'):  # Realiza a divisão em tags da entrada informada
        texto = entrada[2:]  # remove a opção :p
        texto = texto.strip()  # remove espaços iniciais e finais
        if texto:
            analizador.set_texto(texto)
            if analizador.analizar(tags):
                # caso não tiver arquivo para saida, imprimir em tela
                if arq_saida:
                    escrever_resul.escrever(arq_saida, ' '.join(analizador.get_resultado()))
                    Logs.info('Resultado salvo em arquivo!')
                else:
                    print(analizador.get_resultado())

    elif entrada.startswith(':a') or entrada.startswith(':A'):  # Lista as definições formais dos autômatos em memória
        print('Lista as definições formais dos autômatos em memória')

    elif entrada.startswith(':l') or entrada.startswith(':L'):  # Lista as definições de tag válidas
        for tag in tags.get_todas_tags():
            print(f'{tag} {tags.get_tag(tag)}')

    elif entrada.startswith(':s') or entrada.startswith(':S'):  # Salvar as tags
        nome_arquivo = entrada[2:]  # remove a opção :s
        nome_arquivo = nome_arquivo.strip()  # remove espaços iniciais e finais
        if nome_arquivo:
            conteudo_saida = ''
            for tag in tags.get_todas_tags():
                conteudo_saida += tag + ' ' + tags.get_tag(tag) + '\n'
            EscritaArquivos.escrever_static(nome_arquivo, conteudo_saida)
        else:
            Logs.error('Arquivo de saida não fornecido!')

    elif entrada.startswith(':q') or entrada.startswith(':Q'):  # Sair do programa
        escrever_resul.fechar_arquivo()
        break

    elif entrada.startswith(':'):  # Entrada inválida
        Logs.info('Entrada inválida!')

    else:  # Inserção de tag
        if ': ' in entrada:
            tag = entrada.split(': ', 1)  # divide a tags em nome_tag (tag[0]) e a tag em si (tag[1])
            tag = [i.strip() for i in tag]  # remove possiveis espaços iniciais e finais
            tags.adicionar_tag(tag[0].upper(), tag[1])
        else:
            Logs.error('Formato inválido de tag!')