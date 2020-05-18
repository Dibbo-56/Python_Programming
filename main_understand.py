'''
   Every module has __name__ a special variable. When a module is imported
   then it is set to that module name, but the whole module is run like
   python module.py, then it is set to __main__, so then the if condition
   is true as "__name__" == "__main__".
'''

def main():
    print("This is main function")


if "__name__" == "__main__":
    main()
