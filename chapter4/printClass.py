import sys


def print_file(the_list, indent= False, level=0, fh=sys.stdout): #sys.stdout- standart output
        for i in the_list:
            if isinstance(i, list):
                print_file(i, indent, level+1, fh)
            else:
                if indent:
                    for j in range(level):
                        print("\t", end=" ", file=fh)
                print(i, file=fh)
