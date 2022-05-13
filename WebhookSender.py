import requests
import colorama 
from colorama import Fore


#If you change the title without changing the code your a fucking faggot
usern = input(Fore.RED + "What would you like the webhook name to be: ")

msgcont = input(Fore.RED + "Enter non embed message cont (you can leave blank): ")

embdesc = input(Fore.RED + "Enter the message within the embed: ")

url = input(Fore.WHITE + "Please Input Your URL Here: ")

#the msgcont is what will be in plain text (not embeded)
data = {
    "content" : msgcont,
    "username" : usern
}

#all the embed data and shit like what the embed will say
data["embeds"] = [
    {
        "description" : embdesc,
        "title" : "Message Sender By arcry#8651"
    }
]
#posts to the url

result = requests.post(url, json = data)
#error messages if it broken

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Message Sent Successfully".format(result.status_code))