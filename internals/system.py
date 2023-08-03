from rich.console import Console
from rich.table import Table
import random
import yaml
import re
import os

console = Console()

def print_info(message):
    console.print(f"[yellow][INFO][/yellow] {message}")

def print_debug(message):
    console.print(f"[blue][DEBUG][/blue] {message}")

def print_error(message):
    console.print(f"[bold red]❌ {message}")

def print_success(message):
    console.print(f"[bold green]✅ {message}")

def print_info(message):
    console.print(f"[yellow][INFO][/yellow] {message}")
def print_alert(message):
    console.print(f"[bold red][ALERT][/bold red] {message}")

def print_banner():
    banner = r"""
                                /T /I
                                / |/ | .-~/
                            T\ Y  I  |/  /  _
            /T               | \I  |  I  Y.-~/
            I l   /I       T\ |  |  l  |  T  /
        T\ |  \ Y l  /T   | \I  l   \ `  l Y
    __  | \l   \l  \I l __l  l   \   `  _. |
    \ ~-l  `\   `\  \  \\ ~\  \   `. .-~   |
    \   ~-. "-.  `  \  ^._ ^. "-.  /  \   |
    .--~-._  ~-  `  _  ~-_.-"-." ._ /._ ." ./
    >--.  ~-.   ._  ~>-"    "\\   7   7   ]
    ^.___~"--._    ~-{  .-~ .  `\ Y . /    |
    <__ ~"-.  ~       /_/   \   \I  Y   : |
    ^-.__           ~(_/   \   >._:   | l______
        ^--.,___.-~"  /_/   !  `-.~"--l_ /     ~"-.                 + ================================================== +
                (_/ .  ~(   /'     "~"--,Y   -=b-. _)               + [bold yellow]H[/bold yellow].[bold yellow]A[/bold yellow].[bold yellow]W[/bold yellow].[bold yellow]K[/bold yellow] [bold yellow]Eyes[/bold yellow] - [bold blue]Highly Advanced Watchful Keeper Eyes[/bold blue] +
                (_/ .  \  :           / l      c"~o \               + ================================================== +
                    \ /    `.    .     .^   \_.-~"~--.  )                 
                    (_/ .   `  /     /       !       )/   
                    / / _.   '.   .':      /        '                     Security Automation Tool by [bold red]@rohitcoder[/bold red]
                    ~(_/ .   /    _  `  .-<_                                    
                        /_/ . ' .-~" `.  / \  \          ,z=.
                        ~( /   '  :   | K   "-.~-.______//
                        "-,.    l   I/ \_______{--->._(=====.
                        //(     \  <                  \\
                        /' /\     \  \                 \\
                        .^. / /\     "  }__ //===--`\\
                    / / ' '  "-.,__ {---(==-
                    .^ '       :  T  ~"   ll       
                    / .  .  . : | :!        \\
                (_/  /   | | j-"             ~^~^
                    ~-<_(_.^-~"
    """
    console.print(banner)

def get_patterns_from_file(file_path):
    with open(file_path, 'r') as file:
        patterns = yaml.safe_load(file)
        return patterns

def match_strings(content):
    matched_strings = []
    fingerprint_file = 'fingerprint.yml'
    patterns = get_patterns_from_file(fingerprint_file)

    for pattern_name, pattern_regex in patterns.items():
        found = {} 
        matches = re.findall(pattern_regex, content)
        if matches:
            found['pattern_name'] = pattern_name
            found['matches'] = matches
            found['sample_text'] = content[:50]
            matched_strings.append(found)
    return matched_strings

def should_exclude_file(file_name, exclude_patterns, exclude_names):
    _, extension = os.path.splitext(file_name)
    if extension in exclude_patterns:
        return True
    for name in exclude_names:
        if name in file_name:
            return True
    return False


def list_all_files_iteratively(path, exclude_patterns, exclude_names):
    for root, dirs, files in os.walk(path):
        for file in files:
            if not should_exclude_file(file, exclude_patterns, exclude_names):
                yield os.path.join(root, file)

def read_match_strings(file_path, source):
    content = ''
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except Exception as e:
        pass
    matched_strings = match_strings(content)
    return matched_strings