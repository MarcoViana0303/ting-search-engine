from ting_file_management.file_management import txt_importer
import sys

# if path_file not in instance._queue:
#     instance.enqueue(path_file)
#     lines = txt_importer(path_file)
#     file_data = {
#         "nome_do_arquivo": path_file,
#         "qtd_linhas": len(lines),
#         "linhas_do_arquivo": lines
#     }
#     print(file_data)


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for dict in instance._queue:
        if dict["nome_do_arquivo"] == path_file:
            return None
    doc = txt_importer(path_file)
    dict_doc = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(doc),
        "linhas_do_arquivo": doc,
    }
    instance.enqueue(dict_doc)
    print(dict_doc, file=sys.stdout)


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
