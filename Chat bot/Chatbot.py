from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Jarvis')
bot.set_trainer(ListTrainer)
bot.train([
    "What is your name?",
    "My name is Jarvis :)",
    "Who created you?",
    " i was created by Mr. Vignesh"
])

for files in os.listdir('C:/Users/JV/Desktop/Chat bot/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
	data=open('C:/Users/JV/Desktop/Chat bot/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/' + files , 'r').readlines()
	bot.train(data)
while True:
	message=input("You:")
	if message.strip().lower() !='bye':
		reply=bot.get_response(message)
		print('Jarvis:',reply)
	else:
		print('Jarvis:','bye! have a great day')
		break
