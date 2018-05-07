from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def Chat():
	bot = ChatBot('Jarvis')
	trainer=bot.set_trainer(ListTrainer)
	if request.method=='POST':
		while True:
			message=request.form['User']
			if message.strip().lower() !='bye':
				reply=bot.get_response(message)
				return render_template('Chat.html',reply=reply)
			else:
				return render_template('Chat.html',reply='bye! have a great day')
	return render_template('Chat.html')

if __name__=='__main__':
	app.run(debug=True)