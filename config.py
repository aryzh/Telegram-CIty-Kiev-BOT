# -*- coding: utf-8 -*
# configuration file for Telegram BOT administration team

#bot token from Father bot. Given during registration
token = "238872943:AAFTfiHwlfuldFk9pblWwjI2A8CfQVJsKHU"
#path to upload random city photo. use only english keyboard and digits for photo file names.
path = r"\1"
pathGirls = r"girlsPhoto"
#file with anectods or funny stories
afile = "funny.txt"

helloMessage = "ПривеТ, это Киев, ДеТкА :) Просто спроси и всё узнаешь"

#input data from user will be compared with dictinaries from list
exchangeInputText = open(r"InputTexts\exchange", 'r', encoding='utf-8').readlines()
girlsInputText = open(r"InputTexts\girls", 'r', encoding='utf-8').readlines()
taxiInputText = open(r"InputTexts\taxi", 'r', encoding='utf-8').readlines()
weatherInputText = open(r"InputTexts\weather", 'r', encoding='utf-8').readlines()
funnyInputText = open(r"InputTexts\funny", 'r', encoding='utf-8').readlines()

# bot response is taken from dictinaries
funnyOutput = open("funny.txt", 'r', encoding='utf-8').readlines()


#link to external website to parse weather
weatherURL = r"http://api.wunderground.com/api/476242cbfcd192ce/conditions/lang:RU/q/Ukraine/Kyiv.json"

