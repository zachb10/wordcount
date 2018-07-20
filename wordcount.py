import sys
import string


def wordcount():
	#file = open("pg600.txt")
	
	# Try to open the file.
	file = open(str(sys.argv[1]))
	
	total_number_of_words = 0
	words_dict = {}
	
	for line in file:
			wordlist = line.split()
			for word in wordlist:
				clean_word = word.translate(None, string.punctuation).lower()
				total_number_of_words += 1
				if clean_word not in words_dict:
					words_dict[clean_word] = 1
				else:
					words_dict[clean_word] += 1
	
	
	top_words = []
	
	words_dict['*default*'] = 0
	
	for x in range(0, len(words_dict)):
		current = '*default*' # only used once
		for entry in words_dict:
			if words_dict[entry] > words_dict[current]:
				current = entry
		if current == '*default*':
			pass
		else:
			top_words.append(current)
			top_words.append(words_dict[current])
			words_dict.pop(current)
	
	for x in range(0, len(top_words), 2):
		print top_words[x], top_words[x+1]
	print '\n\tFile: ', sys.argv[1]
	print '\tNumber of individual words: ', len(top_words)/2
	print '\tTotal number of words: ', total_number_of_words, '\n'


try:
	wordcount()
except (IndexError, IOError, TypeError):
	print '\n\tUsage: Please provide the name of a text file as an argument.\n'