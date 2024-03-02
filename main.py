
def count_words(src_file):
    word_count = len(src_file.split())
    return word_count

def count_letters(src_file):
    word_dic = {}
    for word in src_file.split():
        for ch in word.lower():
            if ch in word_dic:
                word_dic[ch] += 1        
            else:
                word_dic[ch] = 1       
    return word_dic

def sort_on(in_dict, val = 0):
    return dict (sorted(in_dict.items(), key=lambda x: x[val], reverse=True))

def get_filepath():
    return "books/frankenstein.txt"

def print_rpt(src_file):
    file_words = count_words(src_file)
    file_path = get_filepath()
    word_dic = count_letters(src_file)

    print(f"--- Begin report of {file_path} ---")
    print(f"{file_words} words found in the document\n")

    sorted_word_dic = sort_on(word_dic,1)

    for key in sorted_word_dic.keys():
        if key.isalpha():
            print(f"The '{key}' charecter was found {sorted_word_dic[key]} times") 
    
    print(f"--- End of report ---")

def main():

    file_path = get_filepath() 
    with open(file_path, "r") as f:
        file_contents = f.read()
    print_rpt(file_contents)

if __name__ == "__main__":
    main()

