from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for dict in instance._queue:
        if dict["nome_do_arquivo"] == path_file:
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
        removed = file["nome_do_arquivo"]
        print(f"Arquivo {removed} removido com sucesso")
    except IndexError:
        print("Não há elementos")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
