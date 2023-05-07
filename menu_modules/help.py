# 345678901234567890123456789012345678901234567890123456789012345678900123456789
class Help(object):
    def __init__(self, help_text):
        self.help_text = help_text

    def display_help(self):
        with open(self.help_text, "r") as f:
            for lines in f:
                print(lines)
            f.close()


main_menu_help = Help("./help/main_menu_help.txt")
view_menu_help = Help("./help/view_menu_help.txt")
view_all_help = Help("./help/view_all_help.txt")



