def decode(message_file):
    # Read the content of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    words = []
 
            # Iterate over each line in the file
    for line in lines:
                # Split the line into number and word
        number, word = line.split()
 
                # Append the word to the list 'words'
        words.append(word)
 
            # Sort the words list in ascending order
    words.sort()
    print(words)
 
            # Create a list to store the lines of the pyramid
    pyramid = []
 
            # Initialize a variable to keep track of the current number
    index = 1
    increment = 2
    pyramid.append(words[0])
 
            # Iterate over each line in the pyramid
    while index < len(words):
                # Get the words for the current line
        index += increment
        line_words = words[index-1]
 
                # Convert the words to a string and append to the pyramid list
        pyramid.append(''.join(line_words))
 
                # Increment the current number
        increment += 1
        # print(current_number)
 
            # Join the lines of the pyramid with newline characters
    decoded_message = '\n'.join(pyramid)
 
            # Return the decoded message
    return decoded_message

# Example usage:
message_file_path = 'coding_qual_input.txt'
decoded_message = decode(message_file_path)
print(decoded_message)