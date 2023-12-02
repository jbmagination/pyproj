def importrl():
    import platform;
    if platform.system() == 'Windows':
        try:
            from pyreadline import Readline; # type: ignore
        except ImportError:
            print('It looks like you don\'t have "pyreadline" installed. You need to install it to run this .py file.')
            import sys;
            sys.exit(1)
    else:
        try:
            import readline;
        except ImportError:
            try:
                import gnureadline as readline; # type: ignore
            except ImportError:
                print('It looks like you don\'t have "gnureadline" installed. You need to install it to run this .py file.')
                import sys;
                sys.exit(1)

def importgnurl():
    importrl()
    if readline and not readline.__doc__.__contains__('GNU'):
        try:
            del readline
            import gnureadline as readline; # type: ignore
        except ImportError:
            print('It looks like you don\'t have "gnureadline" installed. You need to install it to run this .py file.')
            import sys;
            sys.exit(1)

def inputfix():
    import sys;
    if not (('__builtin__' in sys.modules) and sys.modules['__builtin__'].raw_input):
        sys.modules['builtins'].raw_input = input
    
def clear():
    import platform;
    import os;
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')