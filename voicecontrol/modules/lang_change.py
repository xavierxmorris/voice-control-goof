# coding=UTF-8

def valid_input(conversation, input):
	lang = conversation.lang_code[:2]

	if lang not in ['pt', 'en']:
		return False

	if lang == 'en':
		return 'language' in input

	if lang == 'pt':
		return 'língua' in input
	
	return False

def process_input(conversation, input):
	lang = conversation.lang_code[:2]

	if lang == 'en':
		if 'portuguese' in input:
			conversation.lang_code = 'pt-PT'
			conversation.say('Ok, falemos como o Camões')
		else:
			conversation.say('Sorry')
	elif lang == 'pt':
		if 'inglês' in  input:
			conversation.lang_code = 'en-US'
			conversation.say('English we are now.')
		else:
			conversation.say('Desculpa')

	return None