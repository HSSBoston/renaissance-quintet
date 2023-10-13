import wikipedia

wikipedia.set_lang("en")
summaryEn = wikipedia.summary("Milky Way", sentences=1, auto_suggest=False)
print(summaryEn)

searchResult = wikipedia.page("Milky Way", auto_suggest=False)
print( searchResult.title )
print( searchResult.url )
print( searchResult.content )
print( searchResult.images )

wikipedia.set_lang("ja")
summaryJa = wikipedia.summary("天の川", sentences=1, auto_suggest=False)
print(summaryJa)



