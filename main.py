def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def print_report(text):
    words = word_count(text)
    chars = character_count(text)
    
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    
    sorted_chars = sorted(chars.items(), key=lambda x: x[1], reverse=True)
    
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
            
    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print_report(file_contents)

if __name__ == "__main__":
    main()