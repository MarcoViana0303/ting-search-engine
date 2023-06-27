def exists_word(word, instance):
    """Aqui irá sua implementação"""
    result = []

    for file_data in instance._queue:
        file_name = file_data["nome_do_arquivo"]
        lines_with_word = []

        for line_number, line in enumerate(
            file_data["linhas_do_arquivo"],
            start=1
         ):
            if word.lower() in line.lower():
                lines_with_word.append({"linha": line_number})

        if lines_with_word:
            file_result = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": lines_with_word
            }
            result.append(file_result)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
