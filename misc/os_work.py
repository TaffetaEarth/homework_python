import os
import string


def file_check(filepath, mode):
    if os.path.exists(filepath):
        if os.path.isfile(filepath):
            f = open("%s" % filepath, "%s" % mode)
            return f
        else:
            return "Incorrect file"
    else:
        return "Incorrect file"


# print(file_check("kivy_test.py", "r"))


def decorator(func_to_decorate):
    def f():
        print(func_to_decorate.__name__)
        os.uname()
        return func_to_decorate()

    return f


@decorator
def adding():
    return 5 + 9


# print(adding())


def formatting(dir_path, exit_format):
    os.chdir(dir_path)
    exit_format = ''.join([sym if (not sym.isdigit()) else "" for sym in exit_format]).split(".")
    print(exit_format)
    if os.path.isdir(dir_path):
        arr = os.listdir(dir_path)
        for i in range(len(arr)):
            if ''.join([sym if (not sym.isdigit()) else "" for sym in arr[i]]).split(".") != \
                    exit_format:
                print(''.join([sym if (not sym.isdigit()) else "" for sym in arr[i]]).split("."))
                if len(arr) < 9:
                    print(arr[i])
                    print("%s" % exit_format[0] + "%s" % (i + 1) + "." + "%s" % exit_format[1])
                    os.rename(arr[i], "%s" % exit_format[0] + "%s" % (i + 1) + "." + "%s" % exit_format[1])
                if 99 > len(arr) > 9:
                    if i < 9:
                        os.rename(arr[i], "%s" % exit_format[0] + "0" + "%s" % (i + 1) + "." + "%s" % exit_format[1])
                    else:
                        os.rename(arr[i], "%s" % exit_format[0] + "%s" % (i + 1) + "." + "%s" % exit_format[1])
                if 999 > len(arr) > 99:
                    if i < 99:
                        os.rename(arr[i], "%s" % exit_format[0] + "00" + "%s" % (i + 1) + "." + "%s" % exit_format[1])
                    else:
                        os.rename(arr[i], "%s" % exit_format[0] + "%s" % (i + 1) + "." + "%s" % exit_format[1])
                if len(arr) > 999:
                    if i < 999:
                        os.rename(arr[i], "%s" % exit_format[0] + "000" + "%s" % (i + 1) + "." + "%s" % exit_format[1])
                    else:
                        os.rename(arr[i], "%s" % exit_format[0] + "%s" % (i + 1) + "." + "%s" % exit_format[1])


formatting("/home/sirius/fotos", "image000.JPG")
