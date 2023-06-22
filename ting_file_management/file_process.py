from file_management import txt_importer
from queue import Queue


def process(path_file, instance):
    """Aqui irá sua implementação"""
    if not instance:
        data = txt_importer(path_file)
        data_instance = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(data),
            'linhas_do_arquivo': data,
        }
        instance.enqueue(data_instance)
        print(data_instance)
        return data_instance

    for index in range(len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return None

    data = txt_importer(path_file)
    data_instance = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(data),
        'linhas_do_arquivo': data,
    }

    instance.enqueue(data_instance)
    print(data_instance)
    return data_instance


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

# def process(path_file, instance):
#     """Aqui irá sua implementação"""
#     if path_file not in instance._queue:
#         instance.enqueue(path_file)
#         lines = txt_importer(path_file)
#         file_data = {
#             "nome_do_arquivo": path_file,
#             "qtd_linhas": len(lines),
#             "linhas_do_arquivo": lines
#         }
#         print(file_data)
