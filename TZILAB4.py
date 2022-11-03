import matplotlib.pyplot as plt
import string

def show(lett, numblett):
	ax = plt.gca()
	ax.bar(lett, numblett, align='edge') 
	ax.set_xticks(lett)
	plt.show()


def show_comparison(lett, numblett1, lett2, numblett2):
	ax = plt.axes()

	xs = []
	endxs = []
	for i in range(len(lett2)):
		try:
			xs.append(lett.index(lett2[i]))
		except:
			endxs.append(lett2[i])

	xs = endxs + xs


	ax.bar(lett, numblett1, color = 'red', align='edge',zorder = 1, width = -0.4, label = 'ВТ')  
	ax.bar(lett2, numblett2, color = 'blue', align='edge',zorder = 2,width = 0.4, label = 'ШТ')  
	ax.set_xticks(lett+lett2)
	plt.legend(loc='upper right')
	plt.show()



def everyletter(text, showd = True):
	letters = {}

	for i in range(len(text)):
		if letters.get(text[i]) == None:
			letters.update([(text[i],1)])
		else:
			letters.update([(text[i],1+letters[text[i]])])

	sortedDict = dict(sorted(letters.items(),reverse=True, key=lambda x: x[1]))

	lett = []
	numblett = []

	for i in sortedDict.items():
		lett.append(i[0])
		numblett.append(i[1])
	if(showd):
		show(lett, numblett)
	return [ lett, numblett ]

def everybigram(text, showd = True, bigrams = []):
	letters = {}
	if len(bigrams) == 0:
		for i in range(0,len(text)-1,1):
			if letters.get(text[i]+text[i+1]) == None:
				letters.update([(text[i]+text[i+1],1)])
			else:
				letters.update([(text[i]+text[i+1],1+letters[text[i]+text[i+1]])])

		sortedDict = dict(sorted(letters.items(),reverse=True, key=lambda x: x[1]))
		
		lett = []
		numblett = []

		for i in sortedDict.items():
			lett.append(i[0])
			numblett.append(i[1])
			if len(lett) > 15:
				break
		if(showd):
			show(lett, numblett)
		return [ lett, numblett ]
	else:
		for i in bigrams:
			letters.update([(i,0)])
		for i in range(0,len(text)-1,1):
			if letters.get(text[i]+text[i+1]) != None:
				letters.update([(text[i]+text[i+1],1+letters[text[i]+text[i+1]])])

		sortedDict = dict(sorted(letters.items(),reverse=True, key=lambda x: x[1]))
		lett = []
		numblett = []

		for i in sortedDict.items():
			lett.append(i[0])
			numblett.append(i[1])
		if(showd):
			show(lett, numblett)
		return [ lett, numblett ]



def everytrigram(text, showd = True, trigrams = []):
	letters = {}

	if len(trigrams) == 0:
		for i in range(0,len(text)-2,1):
			if letters.get(text[i]+text[i+1]+text[i+2]) == None:
				letters.update([(text[i]+text[i+1]+text[i+2],1)])
			else:
				letters.update([(text[i]+text[i+1]+text[i+2],1+letters[text[i]+text[i+1]+text[i+2]])])

		sortedDict = dict(sorted(letters.items(),reverse=True, key=lambda x: x[1]))
		
		lett = []
		numblett = []

		for i in sortedDict.items():
			lett.append(i[0])
			numblett.append(i[1])
			if len(lett) > 15:
				break
		if(showd):
			show(lett, numblett)
		return [ lett, numblett ]
	else:
		for i in trigrams:
			letters.update([(i,0)])
		for i in range(0,len(text)-2,1):
			if letters.get(text[i]+text[i+1]+text[i+2]) != None:
				letters.update([(text[i]+text[i+1]+text[i+2],1+letters[text[i]+text[i+1]+text[i+2]])])

		sortedDict = dict(sorted(letters.items(),reverse=True, key=lambda x: x[1]))
		
		lett = []
		numblett = []

		for i in sortedDict.items():
			lett.append(i[0])
			numblett.append(i[1])
		if(showd):
			show(lett, numblett)
		return [ lett, numblett ]


def vijener_code(text, code_key):
	alphabet = string.ascii_uppercase[0:26] + " '-,.;"
	result=''
	for i in range(len(text)):
		code_key_sumbol = alphabet.find( code_key[i%len(code_key)] )
		result += alphabet[ ( code_key_sumbol + alphabet.find(text[i]) )%32 ]
	return result

def vijener_decode(text, code_key):
	alphabet = string.ascii_uppercase[0:26] + " '-,.;"
	result=''
	for i in range(len(text)):
		code_key_sumbol = alphabet.find( code_key[i%len(code_key)] )
		result += alphabet[ (  alphabet.find(text[i]) - code_key_sumbol )%32 ]
	return result



if __name__ == '__main__':
	bigrams = "TN  AN  IN  HE  ES  TI  EN  ER  ST  ND  ED  ON  RE  IC  AL  DE  OR  SE  TO  AT  IT  AR  TE  IO  NT  OF  IS  RI  EC  ME  HA  CE  NG  CR  PT  CH  RA  RY  BE  YP  KE  EL  TA  LE".split("  ")
	trigrams = "THE  AND  ION  TIO  YPT  CRY  RYP  ATI  DES  ENT  ING  KEY  PTO  NDA  ALL  TED  ESS  IST  ARD  ISA  EVE  IER  SEC  OGR  GRA  RAP  HAN  USE  FOR  WAS  TRI  TOG  APH  FFI  CHA  PUB  UBL  BLI  ITH  DER  ECT  SUC  URE".split("  ")
	
	t = open("VT2.txt","r")
	text = t.read().replace('\n','')
	t.close()

	code_key = "CHORNYI MARKIIAN"

	#print("Відкритий текст:")
	#print(text)
	#print("\nТекст зашифрований методом Віженера з ключем ["+code_key+"]:")
	#print(vijener_code(text, code_key))

	el1 = everytrigram(text,showd=False)
	el2 = everytrigram(vijener_code(text, code_key) , showd=False)

	show_comparison(el1[0], el1[1], el2[0], el2[1])
