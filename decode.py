def decode(message_file):

    with open(message_file, 'r') as file:
        lines = file.readlines()

    words = []

    for line in lines:
        number, word = line.split()
        words.append(word)

    words.sort()
    print(words)

    pyramid = []

    index = 1
    increment = 2
    pyramid.append(words[0])

    while index < len(words):

        index += increment
        line_words = words[index-1]

        pyramid.append(''.join(line_words))

        increment += 1

    decoded_message = '\n'.join(pyramid)

    return decoded_message

message_file_path = 'coding_qual_input.txt'
decoded_message = decode(message_file_path)
print(decoded_message)