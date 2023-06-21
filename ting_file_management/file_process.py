from file_management import txt_importer
from queue import Queue


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for item in instance.queue:
        if item["nome_do_arquivo"] == path_file:
            return
    lines = txt_importer(path_file)

    if lines is not None:
        file_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines
        }
    instance.enqueue(file_data)
    print(file_data)


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


queue_instance = Queue()
process('statics/arquivo_teste.txt', queue_instance)
remove(queue_instance)
