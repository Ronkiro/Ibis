import colorama

def info(extra):
    print(f"{colorama.Back.BLUE}{colorama.Fore.GREEN}{colorama.Style.BRIGHT}"
          f"INFO:{colorama.Style.RESET_ALL} {colorama.Fore.WHITE}{extra}")

def error(extra):
    print(f"{colorama.Back.RED}{colorama.Fore.WHITE}{colorama.Style.BRIGHT}"
          f"ERROR:{colorama.Style.RESET_ALL} {colorama.Fore.WHITE}{extra}")
