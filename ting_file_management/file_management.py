import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        print('Formato inválido', file=sys.stderr)
        return
    try:
        with open(path_file, 'r') as file:
            lines = file.read().splitlines()
            return lines

    except FileNotFoundError:
        error_message = f"Arquivo {path_file} não encontrado"
        print(error_message, file=sys.stderr)
        return
