# -*- encoding: utf-8 -*-
##############################################################
##  Author: Abdulmumen Naas
##	Description: Arabic Natural Language Processor (Kalam-lp)
##	Version: 0.0.1
##  Copyright (c) 2014 Abdulmumen Naas
#############################################################

import re
import string
from constants import *

class Stemmer:	
	def stemNounPrefix(self, token):
		"""stemNounPrefix: returns bool, Prefix clitic for a noun-specific prefix."""
		prfx_re = [AL_REGX,
				CONJPAL_REGX,
				CONJAL_REGX,
				PAL_REGX,
				CONJ_REGX,
				PSOLO_REGX]

		for rex in prfx_re:
			for regx in rex:
				token_prefix = token[:regx[0]]
				if re.match(regx[1], token_prefix):
					return True, token_prefix
				else:
					continue
		return False, "$"

	def stemNounSuffix(self, token):
		"""stemNounSuffix: returns bool, Suffix clitic for a noun-specific suffix."""
		#suffixes = ""
		sffx_re = [CE_SF_REGX,
				CE_DM_REGX,
				CE_DF_REGX,
				CE_PM_REGX,
				CE_PF_REGX
				]
		for rex in sffx_re:
			for regx in rex:
				token_suffix = token[len(token) - regx[0]:]
				if re.match(regx[1], token_suffix):
					print("Noun-Suffix Found.")
					return True, token_suffix
				else:
					continue
		return False, "$"
	
	def stemVerbPrefix(self, token):
		"""stemVerbPrefix: return bool, Prefix clitic for a verb-specific prefix."""
		prfx_re = [CONJPV_REGX,
				CONJ_REGX,
				SAWFA_REGX,
				PVSOLO_REGX,
				PSOLO_REGX,
				]

		for rex in prfx_re:
			for regx in rex:
				token_prefix = token[:regx[0]]
				if re.match(regx[1], token_prefix):
					print("Verb-Prefix Found.")
					sffx_found, verb_sffx = self.stemVerbSuffix(token)
					if sffx_found:
						return True, token_prefix
					else:
						continue
				else:
					continue
		return False, "$"
		
	def stemVerbSuffix(self, token):
		"""stemVerbSuffix: return bool, Suffix clitic for a verb-specific suffix."""
		sffx_re = [POSPRON1_REGX,
				POSPRON2_REGX,
				POSPRON3_REGX]

		for rex in sffx_re:
			for regx in rex:
				token_suffix = token[len(token) - regx[0]:]
				if re.match(regx[1], token_suffix):
					print("Verb-Suffix Found.")
					return True, token_suffix
				else:
					continue
		return False, "$"

	def stemPrefix(self, token):
		"""stemPrefix: return bool,Prefix for a given token."""
		prfxes = [CONJPAL_REGX,
				CONJAL_REGX,
				PAL_REGX,
				CONJSPV_REGX,
				AL_REGX,
				CONJP_REGX,
				CONJPV_REGX,
				SEENPV_REGX,
				CONJ_REGX,
				P_REGX,
				PV_REGX,]

		for prfx_regx in prfxes:
			for regx in prfx_regx:
				token_prefix = token[:regx[0]]
				if re.match(regx[1], token_prefix):
					if token[regx[0]+1:] < 3:
						continue
					else:
						return True, token_prefix
				else:
					continue
		return False, "$"
	
	def stemSuffix(self,token):
		"""stemSuffix: return bool,Suffix for a given token."""
		sffxes = [POSPRON1_REGX,
				POSPRON2_REGX,
				POSPRON3_REGX,
				CE_SF_REGX,
				CE_DF_REGX,
				CE_DM_REGX,
				CE_PM_REGX,
				CE_PF_REGX,]         

		for sffx_regx in sffxes:
			for regx in sffx_regx:
				token_suffix = token[len(token) - regx[0]:]
				if re.match(regx[1], token_suffix):
					if token[:len(token) - regx[0]] < 3:
						continue
					else:
						return True, token_suffix
				else:
					continue
		return False, "$"
		
	def stemLexeme(self, token, root = False, pattern = False):
		"""stemPattern: return a lexeme(root+pattern)."""
		pass

	def stemWords(self, tokens):
		"""stemWords: returns a word object with its pos parameters."""	
		if not tokens:
			return None
		#if not isinstance(args, list):
		#	return "You must use wordTokenize() before steeming."
		#else:
		#	args = list(args)
		#digits regex pattern
		"""
		digit_regx = re.compile("(?:^|\s)
				([1-9]
				(?:\d*|
				(?:\d{0,2})
				(?:,\d{3})*)
				(?:\.\d*[1-9])
				?|0?\.\d*[1-9]|0)
				(?:\s|$)")
		"""
		#Arabic regex
		AR_regx = re.compile(ur'^[\u0600-\u06FF]+$', re.UNICODE)
		
		stemmed_tokens = list()
		prefixes = "$"
		suffixes = "$"

		for token in tokens:
			if not re.match(AR_regx, token):
				stemmed_tokens.append((prefixes,token,suffixes))
			else:
				if self.matchParticle(token):
					stemmed_tokens.append((prefixes,token,suffixes))
				else:
					#prefixes = "$"
					#suffixes = "$"
					stem = token
					sffx_found = False
					prfx_found = False
					k = tuple()
					sffx_found, suffixes = self.stemSuffix(token)
					prfx_found, prefixes = self.stemPrefix(token)
					prefix_start = ""
					suffix_start = ""
					stem = ""
					if sffx_found and prfx_found:
						stem = token[len(prefixes): len(token) - len(suffixes)]
						#k = (suffixes, stem, prefixes)
					elif prfx_found and not sffx_found:
						stem = token[len(prefixes):]
						#k = (suffixes,stem, prefixes)
					elif sffx_found and not prfx_found:
						stem = token[:len(token) - len(suffixes)]
						#k = (suffixes, stem,prefixes)
					else:
						stem = token
					if stem < 3:
						stem = token
						prefixes = "$"
						suffixes = "$"
						k = (prefixes,stem,suffixes)
						print(len(k))
						stemmed_tokens.append(k)     
					else:
						k = (prefixes,stem,suffixes)
						stemmed_tokens.append(k)
		return stemmed_tokens


def main():
	print "It works"

if __name__ == "__main__":
	main()

