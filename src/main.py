from collections import defaultdict


def find_longest_sequence(word_list):
    adj_list = defaultdict(list)
    word_set = set(word_list)
    longest_sequence = 1
    visited_adj_list = {}

    for word in word_list:
        for i in range(len(word)):
            new_word = word[:i] + word[i+1:]
            if new_word != word and new_word in word_set:
                adj_list[word].append(new_word)

    for word in word_list:
        visited = set()
        queue = [word]
        visited.add(word)
        sequence_index = 0
        vertex_list = []
        while queue:
            vertex = queue.pop(0)
            vertex_list.append(vertex)
            if vertex not in visited_adj_list:
                for neighbor in adj_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                        sequence_index += 1
            else:
                sequence_index += visited_adj_list[vertex]
                break
        if sequence_index > longest_sequence:
            longest_sequence = sequence_index
        if word not in visited_adj_list:
            visited_adj_list[word] = sequence_index
            vertex_list = vertex_list[1:]
            if sequence_index != 0:
                for vertex in vertex_list:
                    sequence_index -= 1
                    visited_adj_list[vertex] = sequence_index
    return longest_sequence


def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        word_list = [line.strip() for line in file]
    return word_list


def write_result_to_file(result, file_path):
    with open(file_path, 'w') as file:
        file.write(str(result))
