import oauth2 as oauth
import urllib2 as urllib
import sys
import json
import operator
import urllib2

# See Assignment 1 instructions or README for how to get these credentials
access_token_key = "749698112-ngos04RmeJEBOZyH4WTUsrkrahthmJB9FI6wf2wl"
access_token_secret = "VTWVGwnYqtAjIJF5f5DqX4m3TS6O3Z0F9K5pFlLvrQ"

consumer_key = "93QiZAJ1WyheRaDvDvznEQ"
consumer_secret = "5YhDTdnnYO0Q4Aok3MJmdJRGqoksvCWK87Se6ktfs"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def main():
 added = 0
 count = 0
 
 hi = "hi"
 syl_dict = {}
 unknown = {}
 #print type(hi[0])
 
# opening syllable text file
 sent_file = open(sys.argv[1])
 #tweet_file = open(sys.argv[2])
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
   print added
  print word
  print syl
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
 url = "https://stream.twitter.com/1/statuses/sample.json"
 parameters = []
 response = twitterreq(url, "GET", parameters)

  #print tweetDict
 print '\n \n'
 nameTry = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=python"
 data = json.load(urllib2.urlopen(nameTry))

# print the result
 print data
 for line in response:
  syl = 0				
		#print "in the loop" + str(counter)
		
  tweetDict = json.loads(line)
 
  if tweetDict.has_key("text"):
   
   tweet = tweetDict["text"]
   mock = tweet
   words = tweet.split()
   for word in words:
    if not syl_dict.has_key("".join(c for c in word if c not in ('!','.',':',',','.','#'))):
     mock = ""
     if unknown.has_key(word):
      unknown[word] += 1
     else: 
      unknown[word] = 1

    else:
     syl += syl_dict["".join(c for c in word if c not in ('!','.',':',',','.','#'))]
   if mock == tweet and syl == 17: 
    print tweet
    #print "-" + tweetDict["screen_name"]
  count += 1     
  
  
 for i in range(10):	
		idk = max(unknown.iteritems(), key=operator.itemgetter(1))[0]
		print idk + ' ' + str(unknown[idk])
		unknown.pop(idk, None) 
 print term


if __name__ == '__main__':
  main()
