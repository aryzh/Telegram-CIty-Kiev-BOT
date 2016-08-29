# -*- coding: utf-8 -*
# configuration file for Telegram BOT administration team
import Hide.tokenPrivate
#bot token from Father bot. Given during registration
token = Hide.tokenPrivate.tokenhide


#path to upload random city photo. use only english keyboard and digits for photo file names.
pathKievPhoto = r"kievPhoto"
pathGirls = r"girlsPhoto"
#file with anectods or funny stories
afile = "funny.txt"

helloMessage = "ПривеТ, это Киев, ДеТкА :) Просто спроси и всё узнаешь"

#input text from user  with dictinaries from list
exchangeInputText = open(r"InputTexts/exchange", 'r', encoding='utf-8').readlines()
girlsInputText = open(r"InputTexts/girls", 'r', encoding='utf-8').readlines()
taxiInputText = open(r"InputTexts/taxi", 'r', encoding='utf-8').readlines()
weatherInputText = open(r"InputTexts/weather", 'r', encoding='utf-8').readlines()
funnyInputText = open(r"InputTexts/funny", 'r', encoding='utf-8').readlines()
putinInputText = open(r"InputTexts/putin", 'r', encoding='utf-8').readlines()
deputyInputText = open(r"InputTexts/deputy", 'r', encoding='utf-8').readlines()
kievPhotoInputText = open(r"InputTexts/kievphoto", 'r', encoding='utf-8').readlines()
metroInputText = open(r"InputTexts/metro", 'r', encoding='utf-8').readlines()
mlist = open(r"InputTexts/mlist", 'r', encoding='utf-8').readlines()
astroInputText = "InputTexts/astro"
metroHelpInput = "InputTexts/helpmetro"
tagInputText = open(r"InputTexts/tag", 'r', encoding='utf-8').readlines()
iqInputText = open(r"InputTexts/iq", 'r', encoding='utf-8').readlines()

#data dictinaries for BOT answers to users
funnyOutput = open("funny.txt", 'r', encoding='utf-8').readlines()
putinOutput = open(r"OutputTexts/putin", 'r', encoding='utf-8').readlines()
deputyOutput = open(r"OutputTexts/deputy", 'r', encoding='utf-8').readlines()
metroOutput1 = open(r"OutputTexts/metro1", 'r', encoding='utf-8').readlines()
metroOutput2 = open(r"OutputTexts/metro2", 'r', encoding='utf-8').readlines()
metroOutput3 = open(r"OutputTexts/metro3", 'r', encoding='utf-8').readlines()
tagOutput = "OutputTexts/tag"
iqOutput = open(r"OutputTexts/iq", 'r', encoding='utf-8').readlines()

# Parsing links to external websites to parse
weatherURL = r"http://api.wunderground.com/api/476242cbfcd192ce/conditions/lang:RU/q/Ukraine/Kyiv.json"
astroURL = r"http://img.ignio.com/r/export/utf/xml/daily/com.xml"
