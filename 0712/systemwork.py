import os
import threading


def make_files(quantity, text, path):
    if os.path.isdir(path):
        os.chdir(path)
    else:
        return
    for i in range(quantity):
        file_name = "new_file_%s.txt" % (i + 1)
        os.system("touch %s" % file_name)
        os.system("printf \"" + text + "\" > " + file_name)


def replace_text_in_files(path, text_to_replace, new_text, name):
    name = ''.join([sym if (not sym.isdigit()) else "" for sym in name]).split(".")
    if os.path.isdir(path):
        os.chdir(path)
    threads = []
    arr = os.listdir(path)
    for i in arr:
        if ''.join([sym if (not sym.isdigit()) else "" for sym in i]).split(".") == name:
            i = os.path.realpath(i)
            trd = threading.Thread(target=replacer, args=(i, text_to_replace, new_text))
            threads.append(trd)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def replacer(source, text_to_replace, new_text):
    f = open(source, "r")
    text = f.read()
    if text_to_replace in text:
        text = text.replace(text_to_replace, new_text)
    f = open(source, "w")
    f.write(text)
    f.close()


# make_files(3, "hello", "/home/sirius/homework_python/files")
replace_text_in_files("/home/sirius/homework_python/files", "hello", "<replaced>", "new_file_0.txt")
6