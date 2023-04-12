"""Python functions for JavaScript Trials 1."""
#Tuesdaylab


def output_all_items(items):
    for item in items:
        print(item)


# arr = ['a', 'b', 'c']
# output_all_items(arr)


def get_all_evens(nums):
    evenNums = []

    for num in nums:
        if num % 2 == 0:
            evenNums.append(num)

    return evenNums


# numsArr = [0, 1, 2, 3, 4, 5]
# print(get_all_evens(numsArr))


def get_odd_indices(items):
    result = []

    for ind, item in enumerate(items):
        if ind % 2 != 0:
            result.append(item)

    return result


# oddArr = ['no', 'yes', 'non', 'si', 'nein', 'oui']
# print(get_odd_indices(oddArr))


def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f"{i}. {item}")
        i += 1


# arr = ['dog', 'cat', 'hippo', 'bird']
# print_as_numbered_list(arr)


def get_range(start, stop):
    nums = []

    for num in range(start, stop):
        nums.append(num)

    return nums


# print(get_range(0, 5))


def censor_vowels(word):
    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)

    return "".join(chars)


# print(censor_vowels('Happy Birthday'))


def snake_to_camel(string):
    camelCase = []

    for word in string.split('_'):
        camelCase.append(f'{word[0].upper()}{word[1:]}')

    return ''.join(camelCase)

# print(snake_to_camel('hello_world'))

def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest

# print(longest_word_length(['jellyfish', 'zebra']))

def truncate(string):
    result = []

    for letter in string:
        if (len(result) == 0) or (letter != result[len(result)-1]):
            result.append(letter)

    return ''.join(result)

# print(truncate('hi***!!!! wooow'))

def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1

    return parens == 0

# print(has_balanced_parens('(Oh no!)('))

def compress(string):
    compressed = []

    curr_char = ''
    char_count = 0

    for char in string:
        if char != curr_char:
            compressed.append(curr_char)

            if char_count > 1:
                compressed.append(str(char_count))

            curr_char = char
            char_count = 0
        
        char_count += 1

    compressed.append(curr_char)

    if char_count > 1:
        compressed.append(str(char_count))

    return ''.join(compressed)

print(compress('Hello, world! Cows go moooo...'))