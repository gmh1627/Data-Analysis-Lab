text_only = "[c6]viewelectronic edition via DOIunpaywalled versionreferences & citationsauthority control:&nbsp;export recordBibTeXRISRDF N-TriplesRDF TurtleRDF/XMLXMLdblp key:conf/www/AdriaensA23ask othersGoogleGoogle ScholarSemantic ScholarInternet Archive ScholarCiteSeerXPubPeershare recordTwitterRedditBibSonomyLinkedInFacebookpersistent URL:https://dblp.org/rec/conf/www/AdriaensA23Florian Adriaens, Simon Apers: Testing Cluster Properties of Signed Graphs. WWW 2023: 49-59"
for text in text_only:
    print(text)
for i in range(1 , len(text_only) - 1):
    if text_only[i-1][0:4] == "http" and text_only[i] != ", " and (text_only[i+1] == ", " or text_only[i+1] == ":"):
        #authors.append(text_only[i])
        print(text_only[i-1])
    elif text_only[i][-1] == '.':
        title = text_only[i]
        #print(text_only[i])