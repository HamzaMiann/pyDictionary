"""
Program:    Word definition dictionary.
Author:     Hamza Mian
Version:    0.5
Date:       August 27, 2017
"""

#imports
import json
from difflib import get_close_matches

#get query from user
def getQuery():
    query = input("Please enter a query (q to quit): ")
    return query

#get definition (query results)
def getDef(data, query):
    define = ""
    if query.lower() in data:
        define = data[query.lower()]
    elif query in data:
        define = data[query]
    else:
        matches = get_close_matches(query, data.keys())
        for x in matches:
            yn = input("Did you mean \"" + x + "\"? (y/n/e): ").lower()
            if yn == "y":
                define = data[x]
                query = x
                break
            elif yn == "e" or yn == "exit":
                break
    return (define, query)


#start
data = json.load(open("data.json", "r"))

query = getQuery()
while query != "q":
    result, query = getDef(data, query)
    if result == "":
        print("\n Could not find defintion for \"" + query.title() + "\"\n")
    else:
        print("\n Defintion(s) for \"" + query.title() + "\":\n")
        for x in result:
            print("-- " + x + "\n")
    print("")
    query = getQuery()
#end
