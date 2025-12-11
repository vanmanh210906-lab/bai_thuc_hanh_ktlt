def write_list_to_file(filename, data_list):
    with open(filename, "w") as f:
        for item in data_list:
            f.write(item + "\n")

# Ví dụ dùng
languages = ["Python", "Java", "C++"]
write_list_to_file("languages.txt", languages)
