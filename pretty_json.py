# A query was sent to the Datamuse API, in the string
# https://api.datamuse.com/words?rel_jjb=vegetable
# where the word 'vegetable' is presented to the API.
# --- HERE, brief description of the jjb code used in the query ---
# [code] is a three-letter identifier from the list below.
# [code]  Description                                                                 Example
# jjb     Popular adjectives used to modify the given noun, per Google Books Ngrams:  beach → sandy
#
# The response received from the API, contained between square brackets,
# is assigned to the variable 'data':

data = [
{"word":"green","score":1001},{"word":"other","score":1000},{"word":"fresh","score":999},{"word":"leafy","score":998},{"word":"cooked","score":997},{"word":"only","score":996},{"word":"raw","score":995},{"word":"favorite","score":994},{"word":"popular","score":993},{"word":"excellent","score":992},{"word":"and","score":991},{"word":"common","score":990},{"word":"delicious","score":989},{"word":"important","score":988},{"word":"useful","score":987},{"word":"all","score":986},{"word":"yellow","score":985},{"word":"favourite","score":984},{"word":"culinary","score":983},{"word":"dark","score":982},{"word":"like","score":981},{"word":"mixed","score":980},{"word":"succulent","score":979},{"word":"edible","score":978},{"word":"nutritious","score":977},{"word":"hot","score":976},{"word":"decayed","score":975},{"word":"mere","score":974},{"word":"boiled","score":973},{"word":"wild","score":972},{"word":"valuable","score":971},{"word":"non","score":970},{"word":"wholesome","score":969},{"word":"frozen","score":968},{"word":"native","score":967},{"word":"meat","score":966},{"word":"delicate","score":965},{"word":"solid","score":964},{"word":"organic","score":963},{"word":"sweet","score":962},{"word":"versatile","score":961},{"word":"tasty","score":960},{"word":"dead","score":959},{"word":"strange","score":958},{"word":"animal","score":957},{"word":"bitter","score":956},{"word":"esculent","score":955},{"word":"pure","score":954},{"word":"rich","score":953},{"word":"fat","score":952},{"word":"hardy","score":951},{"word":"soft","score":950},{"word":"pickled","score":949},{"word":"seasonal","score":948},{"word":"tropical","score":947},{"word":"dry","score":946},{"word":"rare","score":945},{"word":"known","score":944},{"word":"light","score":943},{"word":"cultivated","score":942}
]

# 'data' is a list of dictionaries separated by commas, where each dictionary
# contains two key-value pairs,
# key "word" and key "score"
# The objective of this program is to extract all the 'values' related to the
# "word" key and print them as a long string of words separated by commas.

# Find out how many elements has the list 'data'.
data_length = len(data)
# Create an empty list for storing values associated to key "word".
out_list = []

# Using a for loop, extract from each dictionary the 'value' corresponding
# to the key "word" or first key
for x in range(data_length):
    # Take the dictionary stored at 'data[x]', extract the 'value'
    # corresponding to key "word" and append it to 'out_list'.
    out_list.append(data[x]["word"])

# Now, out_list contains all the adjectives related to 'vegetable'
# To convert the list into a string containing all its elements,
# separated by a comma between each other, I will use the 'join()' function.
formatted_list = ", ".join(out_list)
# where
#   formatted_list is the output string
#   ", " is the separator, a comma followed by a space
#   .join is the function applied to out_list to obtain a string.

# Now, let's print the output
print("-------------------------------")
print("A query was sent to the Datamuse API, in the string")
print("https://api.datamuse.com/words?rel_jjb=vegetable")
print("to retrieve a list of adjectives related to the word 'vegetable'.")
print()
print('The API returned JSON objects containing key-value pairs,')
print('the keys being "word" and "score". The values associated')
print('to the "word" key are to be printed.')
print()
print(f"The list of adjectives related to the word 'vegetable' is: {formatted_list}.")
print("-------------------------------")
