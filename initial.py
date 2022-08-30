import nltk
import re
import numpy as numpy
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

f = open("answer_article.txt","r")
read_data = f.read()
f.close()

lemmatizer = nltk.stem.WordNetLemmatizer()
remove_punctuation = dict((ord(punctuation), None) for punctuation in string.punctuation)

greeting_input_texts = ("hey","heys","hello","hi","morning","evening","greetings")
greeting_replie_texts = ["hey","How are you?","hello there","hello world","welcome, how are you"]

how_you_human_reply_texts = ["good", "i'm good", "i am good", "fine", "i'm fine","great","not well", "better"]
how_you_input_texts = ["how are you","how you", "how you doing","how u doing","how r u","how're you"]
how_you_reply_back = ["I'm good!", "Better","I'm always good", "Afraid","Glad after talking to you!"]

love_human_input = ["i love you","love you","i love u","ilu","i'm attracted towards you", "i l u","dear shaily","shaily"]
love_reply_text = ["Ohh! That's great","I'm pleased","I'm feeling lucky","You are awesome"]

marriage_reply_text = ["You may think of marrying the person you love","Love doesn't see any boundaries","Keep loving"]

joke_lists_reply = ["I dreamed I was forced to eat a giant marshmallow, When I woke up, my pillow was gone.","I got another letter from this lawyer today, It said “Final Notice”, Good that he will not bother me anymore.","Manager Asked Santa In An Interview, 'Can You Spell A Word That Has More Than 100 Letters In It?' Santa Replied: ''P-O-S-T-B-O-X.'","Never criticize someone until you’ve walked a mile in their shoes, That way, when you criticize them, they won’t be able to hear you from that far away.","Do I lose when the police officer says papers and I say scissors?","If I got 1 dollar for every failed math exam, I’d be a billionaire by now.","A computer once beat me at chess, but it was no match for me at kick boxing.","As long as there are tests, there will be prayer in schools.","Whenever I find the key to success, someone changes the lock.","Life's like a bird, It's pretty cute until it poops on your head.","The problem isn't that obesity runs in your family, The problem is no one runs in your family."]
def check_love_possibility(text):
	answered = False
	if text.lower() in love_human_input:
		answered = True
		return random.choice(love_reply_text)
	else:
		for word in text.lower().split():
			if word =="marriage" or word=="marry":
				answered=True
				return random.choice(marriage_reply_text)
	if answered==False:
		return False
def check_name_possibility(text):
	answered = False
	split_l = text.lower().split()
	if ("name" in split_l or "named" in split_l) and "shaily" in split_l and ("your" in split_l or "you" in split_l):
		return "Shaily knows it! :)"
	if("what" in split_l and "your" in split_l and "name" in split_l):
		return "I'm Shaily."
	else:
		return False

def check_joke_possibility(text):
	answered = False
	split_l = text.lower().split()
	if ("joke" in split_l):
		return random.choice(joke_lists_reply)+" ;)"
	else:
		return False
def give_reply(user_input,sentence_list,article_words):
	chatbot_response = ''
	sentence_list.append(user_input)
	word_vectors = TfidfVectorizer(tokenizer=RemovePunctuations, stop_words='english')
	vectorized_words = word_vectors.fit_transform(sentence_list)
	similarity_values = cosine_similarity(vectorized_words[-1],vectorized_words)
	similar_sentence_number = similarity_values.argsort()[0][-2]
	similar_vectors = similarity_values.flatten()
	similar_vectors.sort()
	matched_vectors = similar_vectors[-2]
	if(matched_vectors==0):
		chatbot_response = chatbot_response+"I am sorry! I don't understand you"
		# chatbot_response = bot.get_response(user_input)
		return chatbot_response
	else:
		chatbot_response = chatbot_response+sentence_list[similar_sentence_number]
		return chatbot_response

def reply_greeting(text):
	solved = False
	text = text.replace("?","")
	for word in text.split():
		if word.lower() in greeting_input_texts:
			solved = True
			return random.choice(greeting_replie_texts)
	if solved == False:
		if(text.lower() in how_you_human_reply_texts):
			return "That's Great! How can I help you?"
		elif(text.lower() in how_you_input_texts):
			return random.choice(how_you_reply_back)
		else:
			solved = check_love_possibility(text)
			if(solved == False):
				solved = check_name_possibility(text)
			if(solved == False):
				solved = check_joke_possibility(text)
			if(solved==False):
				return "false_1"
			else:
				return solved

def LemmatizeWords(words):
	return [lemmatizer.lemmatize(word) for word in words]
def RemovePunctuations(text):
	return LemmatizeWords(nltk.word_tokenize(text.lower().translate(remove_punctuation)))
def thinking(question):
	content= ''
	#with open('answer_article.txt', 'r') as content_file:
	#	content = content_file.read()
	content = read_data
	question = question.lower()
	sentence_list = nltk.sent_tokenize(content)
	article_words = nltk.word_tokenize(content)
	
	answer = reply_greeting(question)
	if(answer=="false_1"):
		answer = give_reply(question,sentence_list,article_words)
	# speak_eng(answer)
	return answer