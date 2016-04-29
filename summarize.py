from __future__ import unicode_literals
import re
import string

parenthetical = re.compile(r'\([^)]+?\)')
punct_table = {ord(p): ' ' for p in string.punctuation if p not in "-'"}
stops = {'i','me','my','myself','we','our','ours','ourselves','you','your','yours','yourself','yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself','they','them','their','theirs','themselves','what','which','who','whom','this','that','these','those','am','is','are','was','were','be','been','being','have','has','had','having','do','does','did','doing','a','an','the','and','but','if','or','because','as','until','while','of','at','by','for','with','about','against','between','into','through','during','before','after','above','below','to','from','up','down','in','out','on','off','over','under','again','further','then','once','here','there','when','where','why','how','all','any','both','each','few','more','most','other','some','such','no','nor','not','only','own','same','so','than','too','very','s','t','can','will','just','don','should','now','d','ll','m','o','re','ve','y','ain','aren','couldn','didn','doesn','hadn','hasn','haven','isn','ma','mightn','mustn','needn','shan','shouldn','wasn','weren','won','wouldn'}
def summarize(phrase):
    phrase = parenthetical.sub('', phrase)
    phrase = phrase.translate(punct_table)
    words = phrase.split()
    relevant_words = [word for word in words if word not in stops]
    if not relevant_words:
        relevant_words = words
    summary = ' '.join(relevant_words[:10])
    return summary

