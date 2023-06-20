import sys
# import os


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    # file_extension = os.path.splitext(path_file)[1]
    # if file_extension != '.txt':
    #     error_message = "Formato inválido"
    #     sys.stderr.write(error_message + '\n')
    #     sys.exit()
    try:
        if not path_file.endswith('.txt'):
            print('Formato inválido', file=sys.stderr)
            return

        with open(path_file, 'r') as file:
            lines = file.readlines()
            return lines

    except FileNotFoundError:
        error_message = f"Arquivo {path_file} não encontrado"
        print(error_message, file=sys.stderr)
        return


txt_importer('statics/arquivo_teste.txt')
