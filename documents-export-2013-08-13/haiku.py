import sys
import json
import operator
# -*- coding: utf-8 -*-
# this file will print out tweets knowing consisting of 17 syllables



def main():
 added = 0
 count = 0
 
 hi = "hi"
 syl_dict = {}
 unknown = {}
 #print type(hi[0])
 
# opening syllable text file
 sent_file = open(sys.argv[1])
 tweet_file = open(sys.argv[2])
 #print mhyph.txt
 scores = {} # initialize an empty dictionary
 #print sent_file
 for line in sent_file:
  syl = 0
  word = ""
  for char in line:
   #print char
   if char.isalpha():
    word = word + char
    added = 0
   if char == ' ':
    word = word + char
   if (char == ' ' or not char.isalpha()) and added == 0:
    syl = syl + 1
    added = 1
   #print added
  #print word
  #print syl
  syl_dict[word] = syl
  count += 1
 
 syl_dict["a"] = 1
 syl_dict["I"] = 1
 syl_dict["de"] = 1
 syl_dict["to"] = 1
 syl_dict["que"] = 1
 syl_dict["me"] = 1
 syl_dict["la"] = 1
 syl_dict["in"] = 1
 syl_dict["of"] = 1
 syl_dict["is"] = 1
 syl_dict["my"] = 1
 syl_dict["no"] = 1
 syl_dict["en"] = 1
 syl_dict["y"] = 1
 syl_dict["on"] = 1
 syl_dict["el"] = 1
 syl_dict["it"] = 1
 syl_dict["-"] = 0 
 syl_dict["be"] = 1
 syl_dict["te"] = 1
 syl_dict["i"] = 1
 syl_dict["un"] = 1
 syl_dict["so"] = 1
 syl_dict["!"] = 0
 syl_dict["se"] = 0
 syl_dict["I'm"] = 1
 syl_dict[":)"] = 0
 syl_dict["es"] = 1
 syl_dict["at"] = 1
 syl_dict["lo"] = 1
 syl_dict["por"] = 1
 syl_dict["do"] = 1
 syl_dict["."] = 0
 syl_dict["o"] = 1
 syl_dict[","] = 0
 
    
   
 for line in tweet_file.readlines():
  syl = 0				
		#print "in the loop" + str(counter)
		
  tweetDict = json.loads(line)
		
  if tweetDict.has_key("text"):
   
   tweet = tweetDict["text"]
   mock = tweet
   words = tweet.split()
   for word in words:
    if not syl_dict.has_key(word):
     mock = ""
     if unknown.has_key(word):
      unknown[word] += 1
     else: 
      unknown[word] = 1

    else:
     syl += syl_dict[word]
   if mock == tweet: 
    print tweet
  count += 1     
  """if count == 100:
   break"""	
  
 """for i in range(10):	
		idk = max(unknown.iteritems(), key=operator.itemgetter(1))[0]
		print idk + ' ' + str(unknown[idk])
		unknown.pop(idk, None) """
  #print term

if __name__ == '__main__':
    main()
