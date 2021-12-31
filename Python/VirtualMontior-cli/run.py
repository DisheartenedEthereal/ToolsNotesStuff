import os 
import time
import socket 
import npyscreen
class Manager:
    def __init__(self,ip,password):
        self.ip = ip
        self.password = password
    def testvalidity(self,ip):
        """checks if host is up"""
        if os.system("ping -q -c 1 " + ip+" > log.txt") == 0:
            ipvalid = True
            return ipvalid
        else:
            ipvalid = False
            return ipvalid
    def sshopen(self,ip):
        """checks if port 22 is open on said ip"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1',80))
        if result == 0 :
            sshport = True
            return sshport
        else:
            sshport = False
            return sshport
class config:
    pass


class Mainshell:
    def __init__(self,shellnumber):
        self.shellnumber = shellnumber
    def startshell(self):
        pass

class DefaultTheme(npyscreen.ThemeManager):
    default_colors = {
    'DEFAULT'     : 'WHITE_BLACK',
    'FORMDEFAULT' : 'WHITE_BLACK',
    'NO_EDIT'     : 'BLUE_BLACK',
    'STANDOUT'    : 'CYAN_BLACK',
    'CURSOR'      : 'WHITE_BLACK',
    'CURSOR_INVERSE': 'BLACK_WHITE',
    'LABEL'       : 'GREEN_BLACK',
    'LABELBOLD'   : 'WHITE_BLACK',
    'CONTROL'     : 'YELLOW_BLACK',
    'IMPORTANT'   : 'GREEN_BLACK',
    'SAFE'        : 'GREEN_BLACK',
    'WARNING'     : 'YELLOW_BLACK',
    'DANGER'      : 'RED_BLACK',
    'CRITICAL'    : 'BLACK_RED',
    'GOOD'        : 'GREEN_BLACK',
    'GOODHL'      : 'GREEN_BLACK',
    'VERYGOOD'    : 'BLACK_GREEN',
    'CAUTION'     : 'YELLOW_BLACK',
    'CAUTIONHL'   : 'BLACK_YELLOW',
    }
class TestApp(npyscreen.NPSApp):
    def main(self):
        npyscreen.setTheme(npyscreen.Themes.DefaultTheme)
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F  = npyscreen.Form(name = "Virtual Manager CLI",)
        # t  = F.add(npyscreen.TitleText, name = "Text:",)
        # fn = F.add(npyscreen.TitleFilename, name = "Filename:")
        # fn2 = F.add(npyscreen.TitleFilenameCombo, name="Filename2:")
        # dt = F.add(npyscreen.TitleDateCombo, name = "Date:")
        # s  = F.add(npyscreen.TitleSlider, out_of=12, name = "Slider")
        # ml = F.add(npyscreen.MultiLineEdit,
        #        value = """try typing here!\nMutiline text, press ^R to reformat.\n""",
        #        max_height=5, rely=9)
        # ms = F.add(npyscreen.TitleSelectOne, max_height=4, value = [1,], name="Pick One",
        #         values = ["Option1","Option2","Option3"], scroll_exit=True)
        # ms2= F.add(npyscreen.TitleMultiSelect, max_height =-2, value = [1,], name="Pick Several",
        #         values = ["Option1","Option2","Option3"], scroll_exit=True)

        # This lets the user interact with the Form.
        F.edit()

        # print(ms.get_selected_objects())

if __name__ == "__main__":
    App = TestApp()
    App.run()