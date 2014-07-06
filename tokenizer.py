# -*- encoding: utf-8 -*-
##############################################################
##  Author: Abdulmumen Naas
##	Description: Arabic Natural Language Processor (Kalam-lp)
##	Version: 0.0.1
##  Copyright (c) 2014 Abdulmumen Naas
##############################################################
import re
import string
from constants import *

class Tokenizer:
	@classmethod
	def wordTokenize(self, s, xPunct= False):
		"""wordTokenize: return a list words as tokens from a raw of text."""
		if not s or s == "":
			return None

		punct_regex = re.compile(r"[%s\s]+" % re.escape(string.punctuation))
		w_regex = re.compile(r"[\w]+|[%s]" % re.escape(string.punctuation))	
		#_TODO_: Adding arabic punctuations
		
		if not xPunct:
			#Not exclude punctuation
			tokens = re.findall(w_regex, s)
			return tokens
		elif xPunct:
			r = punct_regx.sub(" ", s)
			tokens = r.split()
			return tokens
		else:
			return None


def main():
	print "It works"

if __name__ == "__main__":
	main()

