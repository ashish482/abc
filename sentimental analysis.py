import urllib







def sentimentalAnalysis(text):
    encoded_text=urllib.quote(text)
    API_Call='http;//sentdex.com/api/api.php?text='+encoded_text+'&auth='+sentdexAuth
    output=urllib.urlopen(API_Call).read()
    return output



sentimentRating= sentimentalAnalysis(tweet)
