from os.path import isfile
import sys

# if not path_file.endswith('.txt'):
#     print('Formato inválido', file=sys.stderr)
#     return
# try:
#     with open(path_file, 'r') as file:
#         lines = file.read().splitlines()
#         return lines

# except FileNotFoundError:
#     error_message = f"Arquivo {path_file} não encontrado"
#     print(error_message, file=sys.stderr)
#     retur


def txt_importer(path_file):
    if not isfile(path_file):
        return print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
    elif not path_file.endswith('.txt'):
        return print('Formato inválido', file=sys.stderr)
    doc = open(path_file)
    return doc.read().split('\n')
