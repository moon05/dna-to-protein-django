from Bio.Seq import Seq
from Bio import SeqIO
import time

def KMPSearch(pat, txt): 
	M = len(pat) 
	N = len(txt) 

	# create lps[] that will hold the longest prefix suffix  
	# values for pattern 
	lps = [0]*M 
	j = 0 # index for pat[] 

	# Preprocess the pattern (calculate lps[] array) 
	computeLPSArray(pat, M, lps) 

	i = 0 # index for txt[] 
	while i < N: 
		if pat[j] == txt[i]: 
			i += 1
			j += 1

		if j == M: 
			return (i-j)
			j = lps[j-1] 

		# mismatch after j matches 
		elif i < N and pat[j] != txt[i]: 
			# Do not match lps[0..lps[j-1]] characters, 
			# they will match anyway 
			if j != 0: 
				j = lps[j-1] 
			else: 
				i += 1
	return -1
  
def computeLPSArray(pat, M, lps): 
	len = 0 # length of the previous longest prefix suffix 

	lps[0] # lps[0] is always 0 
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1 
	while i < M: 
		if pat[i]== pat[len]: 
			len += 1
			lps[i] = len
			i += 1
		else: 
			# This is tricky. Consider the example. 
			# AAACAAAA and i = 7. The idea is similar  
			# to search step. 
			if len != 0: 
				len = lps[len-1] 

			# Also, note that we do not increment i here 
			else: 
				lps[i] = 0
				i += 1
	return -1

def check_match(small_string, source):
	s = Seq(small_string)
	res = KMPSearch(s, source)
	return res

genomeFiles = {
				0: {"file_loc": "./dnatoprotein/protein_files/NC_000852.fasta", "name": "NC_000852: Paramecium bursaria Chlorella virus 1, complete genome" },
				1: {"file_loc": "./dnatoprotein/protein_files/NC_007346.fasta", "name": "NC_007346: Emiliania huxleyi virus 86, complete genome"},
				2: {"file_loc": "./dnatoprotein/protein_files/NC_008724.fasta", "name": "NC_008724: Acanthocystis turfacea Chlorella virus 1, complete genome"},
				3: {"file_loc": "./dnatoprotein/protein_files/NC_009899.fasta", "name": "NC_009899: Paramecium bursaria Chlorella virus AR158, complete genome"},
				4: {"file_loc": "./dnatoprotein/protein_files/NC_014637.fasta", "name": "NC_014637: Cafeteria roenbergensis virus BV-PW1, complete genome"},
				5: {"file_loc": "./dnatoprotein/protein_files/NC_016072.fasta", "name": "NC_016072: Megavirus chiliensis, complete genome"},
				6: {"file_loc": "./dnatoprotein/protein_files/NC_020104.fasta", "name": "NC_020104: Acanthamoeba polyphaga moumouvirus, complete genome"},
				7: {"file_loc": "./dnatoprotein/protein_files/NC_023423.fasta", "name": "NC_023423: Pithovirus sibericum isolate P1084-T, complete genome"},
				8: {"file_loc": "./dnatoprotein/protein_files/NC_023719.fasta", "name": "NC_023719: Bacillus phage G, complete genome"},
				9: {"file_loc": "./dnatoprotein/protein_files/NC_027867.fasta", "name": "NC_027867: Mollivirus sibericum isolate P1084-T, complete genome"}
			}

#not taking reverse complement since
#search string is not gonna be based on genes
def search(dna_string):
	for values in genomeFiles.values():
		filename = values["file_loc"]
		r = ""
		for records in SeqIO.parse(filename, "fasta"):
			print (records.id)
			r = records.seq
			print (type(r))
			res = check_match(dna_string, r)
			if res != -1:
				print ({"match_loc": res, "name": values["name"]})
				return {"match_loc": res, "name": values["name"]}
			else:
				continue 
	return -1


#for test
# first = "CAAATCAAATTCCTCAATCGGATCTCCTTCTCTTAGAAGAATACCCCAAATCAA"
# second = "ACTGTAATGTATTGCAATATCAGGGAATTATCCAAAAATCATAAATGTGCCGTCGGTGAGTTTATAACACCCGAGAACTATAACACTGTAACATTGAAGAAATGAAAATTCTTGTGATGCTATTTGTATGTATGTTGTATGCAATTGCCGACTGTATTGTTAAGTGCGTCGGTCGCCCGGCTCATAAAAAATATTATACTTTAAATAAAAGATAA"
# third = "GATTCGTAACGATATTCGATCTTTGGATAAAATGTTGCCTTAACTAGACCGTTACTTTCTCCACCAATTGTGATTCCAGCCCGATACGCTTGATTACTCGTCTCACGGAAAAAGGTGAACTTTCGATCAATGTAAGCGGGTCTTTTGACCACAATGAAATCGTTAGCGGGAATTCTCCATTTTCCCACATGTTCTCCTTCGATTTCAAGACTAA"
# print (search(first))