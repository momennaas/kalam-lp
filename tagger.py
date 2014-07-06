# -*- encoding: utf-8 -*-
##############################################################
##  Author: Abdulmumen Naas
##	Description: Arabic Natural Language Processor (Kalam-lp)
##	Version: 0.0.1
##	Copyright (c) 2014 Abdulmumen Naas
#############################################################

import re
import string
from constants import *

class Tagger:
	def prefixTagger(self, token):
		"""taggedPrefix: returns a part-of-speech tagged prefix."""
		if not token:
			return False, None

		for rex in CONJPAL_REGX:
			#CONJ+P+AL(Article)
			prfx = token[:rex[0]]
			if re.match(rex[1], prfx):
				prefix_pos = "AL+P+CONJ"
				return True, prefix_pos
			else:
				continue
		
		for rex in CONJAL_REGX:
			prfx = token[:rex[0]]			
			#CONJ+AL(Article)
			if re.match(rex[1], prfx):
				prefix_pos = "AL+CONJ"
				return True, prefix_pos

			else:
				continue

		for rex in PAL_REGX:
			prfx = token[:rex[0]]			
			#P+AL(Article)
			if re.match(rex[1], prfx):
				if token[rex[0]+1:] < 3:
					continue
				else:
					prefix_pos = "AL+P"
					return True, prefix_pos	
			else:
				continue
			
		for rex in CONJSPV_REGX:
			prfx = token[:rex[0]]			
			#CONJ+AL(Article)
			if re.match(rex[1], prfx):
				prefix_pos = "PV+S+CONJ"
				return True, prefix_pos

			else:
				continue
		
		for rex in AL_REGX:
			prfx = token[:rex[0]]			
			if re.match(rex[1], prfx):
				if token[rex[0]+1:] < 3:
					continue
				else:	
					prefix_pos = "AL"
					return True, prefix_pos
				
			else:
				continue
		
		for rex in CONJP_REGX:
			prfx = token[:rex[0]]			
			if re.match(rex[1], prfx):
				if token[rex[0]+1:] < 3:
					continue
				else:
					prefix_pos = "P+CONJ"
					return True, prefix_pos
			else:
				continue
		
		for rex in CONJPV_REGX:
			prfx = token[:rex[0]]			
			if re.match(rex[1], prfx):
				if token[rex[0]+1:] < 3:
					continue
				else:
					prefix_pos = "PV+CONJ"
					return True, prefix_pos
			else:
				continue
		
		for rex in SEENPV_REGX:
			prfx = token[:rex[0]]			
			if re.match(rex[1], prfx):
				if token[rex[0]+1:] < 3:
					continue
				else:
					prefix_pos = "PV+S"
					return True, prefix_pos
			else:
				continue
		
		for rex in CONJ_REGX:
			prfx = token[:rex[0]]			
			if re.match(rex[1], prfx):
				if token[rex[0]+1:] < 3:
					continue
				else:
					prefix_pos = "CONJ"
					return True, prefix_pos
			else:
				continue

		for rex in P_REGX:
			prfx = token[:rex[0]]			
			if re.match(rex[1], prfx):
				if token[rex[0]+1:] < 3:
					continue
				else:
					prefix_pos = "P"
					return True, prefix_pos
			else:
				continue
		
		for rex in PV_REGX:
			prfx = token[:rex[0]]			
			if re.match(rex[1], prfx):
				if token[rex[0]+1:] < 3:
					continue
				else:
					prefix_pos = "PV"
					return True, prefix_pos
			else:
				continue

		return False, None

	
	def suffixTagger(self, token):
		"""taggedSuffix: returns a part-of-speech tagged suffix."""
		if not token:
			return False, None
		

		for rex in POSPRON1_REGX:
			sffx = token[len(token) - rex[0]:]
			if re.match(rex[1], sffx):
				suffix_pos = "POSPRON1"
				return True, suffix_pos
			else:
				continue
					
		for rex in POSPRON1_REGX:
			sffx = token[len(token) - rex[0]:]
			if re.match(rex[1], sffx):
				suffix_pos = "POSPRON2"
				return True, suffix_pos
			else:
				continue
		
		for rex in POSPRON1_REGX:
			sffx = token[len(token) - rex[0]:]
			if re.match(rex[1], sffx):
				suffix_pos = "POSPRON3"
				return True, suffix_pos
			else:
				continue
	
		for rex in CE_SF_REGX:
			if re.match(rex[1], sffx):
				suffix_pos = "CESF"
				return True, suffix_pos		
			else:
				continue
			
		for rex in CE_DM_REGX:
			sffx = token[len(token) - rex[0]:]
			if re.match(rex[1], sffx):
				suffix_pos = "CEDM"
				return True, suffix_pos		
			else:
				continue
						
		for rex in CE_DF_REGX:
			sffx = token[len(token) - rex[0]:]
			if re.match(rex[1], sffx):
				suffix_pos = "CEDF"
				return True, suffix_pos		
			else:
				continue

		for rex in CE_PM_REGX:
			sffx = token[len(token) - rex[0]:]
			if re.match(rex[1], sffx):
				suffix_pos = "CEPM"
				return True, suffix_pos				
			else:
				continue
					
		for rex in CE_DM_REGX:
			sffx = token[len(token) - rex[0]:]
			if re.match(rex[1], sffx):
				suffix_pos = "CEPF"
				return True, suffix_pos					
			else:
				continue

		return False, None

	
	def lexemeTagger():
		"""taggedLexeme: returns a lexeme root+pattern."""
		patterns = []
		pass
	
	def particleTagger(self, token):
		"""taggedParticle: returns a POS tagged particle."""
		if not token:
			return False, None
		
		#Prepositions
		for rex in PREP_REGX:
			if re.match(rex[1], token):
				p_pos = "P"
				return True, p_pos					
			else:
				continue
		#Conjunctions
		for rex in CONJ_REGX:
			if re.match(rex[1], token):
				p_pos = "CONJ"
				return True, p_pos					
			else:
				continue
		#Conditions
		for rex in COND_REGX:
			if re.match(rex[1], token):
				p_pos = "COND"
				return True, p_pos					
			else:
				continue
		#Vocals
		for rex in VOC_REGX:
			if re.match(rex[1], token):
				p_pos = "VOC"
				return True, p_pos					
			else:
				continue
		#Negative
		for rex in NEG_REGX:
			if re.match(rex[1], token):
				p_pos = "NEG"
				return True, p_pos					
			else:
				continue
		#Exceptions
		for rex in EXP_REGX:
			if re.match(rex[1], token):
				p_pos = "EXP"
				return True, p_pos					
			else:
				continue
		
		if len(token) == 1:
			return True, "P"

		return False, None
	
	def nounTagger(self, token):
		"""nounTagger: returns a Noun-specific Part-Of-Speech."""
		#Personal Pronouns
		if not token:
			return False, None

		for rex in PPRON1_REGX:
			if re.match(rex[1], token):
				p_pos = "PPRON1"
				return True, p_pos					
			else:
				continue
		for rex in PPRON2_REGX:
			if re.match(rex[1], token):
				p_pos = "PPRON2"
				return True, p_pos					
			else:
				continue
		for rex in PPRON3_REGX:
			if re.match(rex[1], token):
				p_pos = "PPRON3"
				return True, p_pos					
			else:
				continue
		for rex in DEM_REGX:
			if re.match(rex[1], token):
				p_pos = "DEM"
				return True, p_pos					
			else:
				continue
		
		for rex in DEMLOC_REGX:
			if re.match(rex[1], token):
				p_pos = "DEMLOC"
				return True, p_pos					
			else:
				continue
		for rex in ACC_REGX:
			if re.match(rex[1], token):
				p_pos = "ACC"
				return True, p_pos					
			else:
				continue
		for rex in TENN_REGX:
			if re.match(rex[1], token):
				p_pos = "TENN"
				return True, p_pos					
			else:
				continue
		return False, None


	def verbTagger(self, token):
		"""verbTagger: returns a verb-specific part-of-speech."""
		pass

	def isNoun(self, token, prev_token = None):
		"""isNoun: returns bool if a given token is a noun."""
		#Nouns	
		stemmed_token = self.stemTokens([token,])

		prefix = stemmed_token[0][0]
		stem = stemmed_token[0][1]
		suffix = stemmed_token[0][2]

		prfx_found, prefix_pos = self.prefixTagger(prefix)
		sffx_found, suffix_pos = self.suffixTagger(suffix)
		
		isNoun = False
	
		AL_PAT= re.compile("AL")
		PREP_PAT = re.compile("P")
		CONJ_PAT = re.compile("CONJ")
		#CE_PAT = re.compile("[CESF|CEDF|CEDM|CEPM|CEPF|POSPRON1|POSPRON2|POSPRON3]")
		CESF_PAT = re.compile("CESF")
		CEDF_PAT = re.compile("CEDF")
		CEDM_PAT = re.compile("CEDM")
		CEPF_PAT = re.compile("CEPF")
		CEPM_PAT = re.compile("CEPM")
		POSPRON1_PAT = re.compile("POSPRON1")
		POSPRON2_PAT = re.compile("POSPRON2")
		POSPRON3_PAT = re.compile("POSPRON3")
		PPRON1_PAT = re.compile("PPRON1")
		PPRON2_PAT = re.compile("PPRON2")
		PPRON3_PAT = re.compile("PPRON3")
		ACC_PAT = re.compile("ACC")
		REL_PAT = re.compile("REL")
		DEM_PAT = re.compile("DEM")
		DEMLOC_PAT = re.compile("DEMLOC")
               
        

		if prfx_found:	
			if AL_PAT.findall(prefix_pos):
				isNoun = True
				return isNoun
			
			elif PREP_PAT.findall(prefix_pos):
				if sffx_found:
					if CESF_PAT.findall(suffix_pos) or CEDF_PAT.findall(suffix_pos) or CEDM_PAT.findall(suffix_pos) or CEPF_PAT.findall(suffix_pos) or CEPM_PAT.findall(suffix_pos):
						isNoun = True
						return isNoun
				else:
					pass
			elif CONJ_PAT.findall(prefix_pos):
				if sffx_found:
					if CESF_PAT.findall(suffix_pos) or CEDF_PAT.findall(suffix_pos) or CEDM_PAT.findall(suffix_pos) or CEPF_PAT.findall(suffix_pos) or CEPM_PAT.findall(suffix_pos):
						isNoun = True
						return isNoun
				else:
					pass
			elif PREP_PAT.findall(prefix_pos) and not self.isVerb(token):
				isNoun = True
				return isNoun
			elif CONJ_PAT.findall(prefix_pos) and not self.isVerb(token):
				pass
			else:
				pass
		elif sffx_found:
			if CESF_PAT.findall(suffix_pos) or CEDF_PAT.findall(suffix_pos) or CEDM_PAT.findall(suffix_pos) or CEPF_PAT.findall(suffix_pos) or CEPM_PAT.findall(suffix_pos):
				isNoun = True
				return isNoun
		else:
			nounFound, noun_pos = self.nounTagger(token)
			if nounFound:
				isNoun = True
				return isNoun

		return isNoun


	def isVerb(self, token, prev_token= None):
		"""isVerb: returns bool if a given token is a verb."""
		stemmed_token = self.stemTokens([token,])	
		prefix = stemmed_token[0][0]
		stem = stemmed_token[0][1]
		suffix = stemmed_token[0][2]

		
		prfx_found, prefix_pos = self.prefixTagger(prefix)
		sffx_found, suffix_pos = self.suffixTagger(suffix)
		isVerb = False
		
		CONJSPV_PAT = re.compile("CONJSPV")
		CONJPV_PAT = re.compile("CONJPV")
		SPV_PAT = re.compile("SPV")		
		CONJ_PAT = re.compile("CONJ")
		PV_PAT = re.compile("PV")
		S_PAT = re.compile("S")
		POSPRON1_PAT = re.compile("POSPRON1")
		POSPRON2_PAT = re.compile("POSPRON2")
		POSPRON3_PAT = re.compile("POSPRON3")

		if prfx_found:	
			if CONJSPV_PAT.findall(prefix_pos) or CONJPV_PAT.findall(prefix_pos) or SPV_PAT.findall(prefix_pos) or CONJ_PAT.findall(prefix_pos) or PV_PAT.findall(prefix_pos) or S_PAT.findall(prefix_pos):
				if sffx_found:
					if POSPRON1_PAT.findall(suffix_pos) or POSPRON2_PAT.findall(suffix_pos) or POSPRON3_PAT.findall(suffix_pos):
						isVerb = True
						return isVerb
					elif not len(stem) < 3:
						isVerb = True
						return isVerb
					else:
						isVerb = False
				else:
					isVerb = True
					return isVerb
			else:
				isVerb = False

		return isVerb


	def isParticle(self, token, prev_token = None):
		"""isParticle: returns bool if a given token a particle."""
		isParticle = False
		particleFound, particle_pos = self.particleTagger(token)
		if particleFound:
			isParticle = True
			return isParticle
		else:
			isParticle = False
		return isParticle
	
	def isForeignWord(self, token, prev_token = None):
		"""isForeignWord: returns bool if a given token is not and arabic word."""
		AR_regx = re.compile(ur'^[\u0600-\u06FF]+$', re.UNICODE)
		isFW = False
		if not re.match(AR_regx, token):
			isFW = True
			return isFW
		else:
			isFW = False
		return isFW

	def isNumber(self, token, prev_token = None):
		"""isNumber: returns bool if a given token is a digit."""
		"""digit_regx = re.compile("(?:^|\s)\
				([1-9] \
				(?:\d*| \
				(?:\d{0,2}) \
				(?:,\d{3})*) \
				(?:\.\d*[1-9]) \
				?|0?\.\d*[1-9]|0) \
				(?:\s|$)")
				"""
		num_pat = re.compile("^[0-9]+$")
		isNumber = False
		if num_pat.findall(token):
			isNumber = True
			return isNumber
		else:
			isNumber = False
		return isNumber

	def isPunctuation(self, token, prev_token = None):
		"""isPunctuation: returns bool if a given token is a punctuation."""
		punc_regx = re.compile(r"[%s\s]+" % re.escape(string.punctuation))
		isPunc = False
		if re.match(punc_regx, token):
			isPunc = True
			return isPunc
		else:
			isPunc = False
		return isPunc

	def isSymbol(self, token, prev_token = None):
		"""isSymbol: returns bool if a given token is a symbol."""
		pass

	def posNounTagger(self, token):
		"""posNounTagger: return noun-specific part-of-speech."""
		#output: t <- (word, case, state,gender, number)
		stemmed_token = self.stemTokens([token,])
		pass

	
	def bayanTagger(self, seg):
		"""bayanTagger: returns a tagged-segment with what does it represent in real world."""


	def posTagger(self, tokens, sep = "+", nouns = False, verbs = False, particles = False):
		"""posTagger: returns part-of-speech tag for a a given word/words."""
		
		if not tokens:
			return False, None

		posed_tokens = list()
		isNoun = False
		isVerb = False
		isParticle = False
		isNumber = False
		isUnkown = False
		for token in tokens:
			#stemmed_token = self.stemTokens([token,])
			if self.isNoun(token):
				pos_token = ur"%s%s%s" % ("N", sep, token)
				posed_tokens.append(pos_token)
				isNoun = True
				print("N-found")
				continue

			elif self.isVerb(token):
				pos_token = ur"%s%s%s" % ("V", sep, token) 				
				posed_tokens.append(pos_token)
				isVerb = True
				print("V-found")
				continue

			elif self.isParticle(token):
				pos_token = ur"%s%s%s" % ("P", sep, token) 
				posed_tokens.append(pos_token)
				isParticle = True
				print("P-found")
				continue

			elif self.isNumber(token):
				pos_token = ur"%s%s%s" % ("NUM", sep, token) 				
				posed_tokens.append(pos_token)
				isNumber = True
				print("NUM-found")
				continue

			else:
				pos_token = ur"%s%s%s" % ("N", sep, token)
				posed_tokens.append(pos_token)
				isNoun = True
				print("N-found")
				continue
		return posed_tokens

def main():
	print "It works"

if __name__ == "__main__":
	main()
