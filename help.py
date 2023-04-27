class Help:
    def __init__(self, name, help_text_file):
        self.name = name
        self.help_text = help_text_file


class MainMenuHelp(Help):
    def __init__(self):
        help_text = open("./help/main_menu_help.txt")
        for help in help_text.readlines():
            print(help)