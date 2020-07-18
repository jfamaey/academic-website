import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

keys = set()

def parse_conference(text):
	d = text.find('.')
	authors = parse_authors(text[:d].strip())
	text = text[d+1:]
	d = text.find('.')
	title = text[:d].strip()
	text = text[d+1:]
	d = text.find('.')
	sub_fields = text[:d].split(", ")
	conference = sub_fields[0].strip()
	year = sub_fields[-1].strip()
	doi = ""
	if text[d+1:].find('doi') != -1:
		doi = text[d+1:-1].split(':')[1].strip()
	
	key = authors[0][1].replace(" ", "") + year
	key_index = ord('a')
	while key + chr(key_index) in keys:
		key_index += 1
	key += chr(key_index)
	keys.add(key)
	
	bibtex = "@inproceedings{" + key + ",\n"
	bibtex += "\tauthor = {"
	for i in range(len(authors)):
		bibtex += authors[i][1] + ", " + authors[i][0]
		if i < len(authors) - 1:
			bibtex += " and "
	bibtex += "},\n"
	bibtex += "\tbooktitle = {" + conference + "},\n"
	bibtex += "\ttitle = {" + title + "},\n"
	if not doi == '':
		bibtex += "\tdoi = {" + doi + "},\n"
	bibtex += "\tyear = {" + year + "}\n"
	bibtex += "}\n"
	return bibtex

def parse_journal(text):
	parts = line.split('.', 3)
	authors = parse_authors(parts[0].strip())
	title = parts[1].strip()
	doi = parts[3].split(':')[1].split(' ')[0].strip()
	parts = parts[2].split(', ')
	journal = parts[0].strip()
	year = parts[2].strip()
	vnp = parse_volume(parts[1].strip())
	
	key = authors[0][1].replace(" ", "") + year
	key_index = ord('a')
	while key + chr(key_index) in keys:
		key_index += 1
	key += chr(key_index)
	keys.add(key)
	
	bibtex = "@article{" + key + ",\n"
	bibtex += "\tauthor = {"
	for i in range(len(authors)):
		bibtex += authors[i][1] + ", " + authors[i][0]
		if i < len(authors) - 1:
			bibtex += " and "
	bibtex += "},\n"
	bibtex += "\tjournal = {" + journal + "},\n"
	bibtex += "\ttitle = {" + title + "},\n"
	if not vnp[0] == '':
		bibtex += "\tvolume = {" + vnp[0] + "},\n"
	if not vnp[1] == '':
		bibtex += "\tnumber = {" + vnp[1] + "},\n"
	if not vnp[2] == '':
		bibtex += "\tpages = {" + vnp[2] + "},\n"
	bibtex += "\tyear = {" + year + "},\n"
	bibtex += "\tdoi = {" + doi + "}\n"
	bibtex += "}\n"
	return bibtex
			
	
def parse_authors(str):
	authors = str.split(', ')
	list = []
	for author in authors:
		i = author.find(' ')
		list.append((author[:i], author[i+1:]))
	return list
	
def parse_volume(str):
	volume = ''
	number = ''
	pages = ''
	pstart = str.find(':')
	nstart = str.find('(')
	if pstart != -1:
		pages = str[pstart + 1:]
		str = str[:pstart]
	if nstart != -1:
		number = str[nstart + 1 : -1]
		str = str[:nstart]
	if (str.isdecimal()):
		volume = str
	return (volume, number, pages)

input = open('journal_papers.txt', encoding="utf8")
for line in input:
	print(parse_journal(line))
	print()
input.close()
	
input = open('conference_papers.txt', encoding="utf8")

for line in input:
	print(parse_conference(line.rstrip('\n')))
	print()