def read_data(file_path):
    file_open = open(file_path, "r")
    data = file_open.readlines()
    list_of_word = []
    for word in data:
        list_of_word.append(word.strip("\n"))
    return list_of_word


def longest_string_chain(data_inputs):
    inputs = sorted(data_inputs, key=len)
    word_chains = {word: 1 for word in inputs}

    for word in word_chains:
        if len(word) == 1:
            continue
        for i in range(len(word)):
            checking_word = word.replace(word[i], '', 1)
            if checking_word in word_chains:
                word_chains[word] = max(word_chains[checking_word] + 1, word_chains[word])

    result_word_chain = max(word_chains.values())
    return result_word_chain


if __name__ == '__main__':
    data = read_data('wchain_1.in')
    result_of_max_chain = longest_string_chain(data)
    print(f"Max chain => {result_of_max_chain}")

    data_2 = read_data('wchain_2.in')
    result_of_max_chain = longest_string_chain(data_2)
    print(f"Max chain => {result_of_max_chain}")

    data_3 = read_data('wchain_3.in')
    result_of_max_chain = longest_string_chain(data_3)
    print(f"Max chain => {result_of_max_chain}")
