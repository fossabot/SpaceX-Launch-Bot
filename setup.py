"""
A Python3 script to help when installing this bot on a new / clean server
"""
from getpass import getuser
from urllib import request
from os import path
import sys

def replacePlaceholderInFiles(filePathList, placeHolder, replaceWith):
    for path in filePathList:
        with open(path, "r") as fin:
            body = fin.read()
        with open(path, "w") as fout:
            fout.write(body.replace(placeHolder, replaceWith))

"""
Each array contains the paths to files that need said values replacing
"""
externalIPFiles = [path.join("services", "nginx", "infoWebServer")]
discordTokenFiles = [path.join("services", "systemd", "SLB.service")]
dblTokenFiles = [path.join("services", "systemd", "SLB.service")]

# Get variables
externalIP = input("Input the IP you want infoWebServer to bind to (leave blank for auto)\n>>")
if externalIP.strip() == "":
    externalIP = request.urlopen("https://ident.me").read().decode("utf8")

discordToken = input("Input your Discord token\n>> ").strip()
dblToken = input("Input your Discord bot list token\n>> ").strip()

print(f"""
Using:
bind IP       : {externalIP}
discord token : {discordToken[0:10]}...{discordToken[-10:]}
dbl token     : {dblToken[0:10]}...{dblToken[-10:]}
""")

if input("Is this correct? y/n ").strip().lower() == "n":
    sys.exit()

print("\nCopying variables to associated files")

replacePlaceholderInFiles(
    externalIPFiles,
    "SERVER-IP",
    externalIP
)
replacePlaceholderInFiles(
    discordTokenFiles,
    "DISCORD-TOKEN",
    discordToken
)
replacePlaceholderInFiles(
    dblTokenFiles,
    "DBL-TOKEN",
    dblToken
)

print("\nDone")
