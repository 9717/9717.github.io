from chatterbot import chatbox
from chatter.trainers import ListTrainer
import os

bot=ChatBot('Trainer')
bot.set_trainer(ListTrainer)

for files in os.listdir('C:\Users\Nandan\Desktop\buiseness urban\chatterbot_corpus\data\english'):

  data=open('C:\Users\Nandan\Desktop\buiseness urban\chatterbot_corpus\data\english'+files,'r').readlines()

bot.train(data)
while true:
message=input('you:')

if message.strip() !='bye':
reply=bot.get.response(message)
print('ChatBot:',reply)
if message.strip()=='bye';
print('ChatBot :'Bye)
break