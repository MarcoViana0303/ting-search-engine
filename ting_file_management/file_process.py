from ting_file_management.file_management import txt_importer
import sys
# from queue import Queue


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for file in instance._queue:
        if file["nome_do_arquivo"] == path_file:
            return None
    lines = txt_importer(path_file)
    files_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }
    instance.enqueue(files_data)
    print(files_data, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""
    try:
        file = instance.dequeue()
        if file is not None:
            removed = file["nome_do_arquivo"]
            print(f"Arquivo {removed} removido com sucesso")
        else:
            print("Não há elementos")
    except IndexError:
        print("Não há elementos")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        files_data = instance.search(position)
        print(files_data, file=sys.stdout)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
        return None


# example = Queue()
# process('statics/arquivo_teste.txt', example)
# file_metadata(example, 0)
