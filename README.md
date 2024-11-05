## Getting the Information: Accessing the API

As mentioned before, there exists a whole world, largely unseen by the average person, of data-exchanging APIs on the web. Let's take a look at one:

 [https://api.datamuse.com/words?rel_jjb=oceanLinks](https://api.datamuse.com/words?rel_jjb=oceanLinks) is an API that supplies adjectives that describe a word supplied by the user.

Take a look at the web address (URL): It shows the domain (`api.datamuse.com`) and the path (`/words`), but then has a question mark (`?`) followed by a name and an equal sign, then finally a value (Another name for the name=value part a **name:value pair**). It turns out that when an API is called, any data needed by the API will be attached to the end of the URL in **name:value** pairs.

The question mark signals where the data begins. Any data that follows the question mark uses a name:value pair format. Recall the purpose of this API (datamuse) is to return a list of adjectives describing a given word. If you look at the **name:value** pair following the question mark, you see `rel_jjb=ocean`. So the name of the data is `rel_jjb` and the value is `'ocean'`. So this particular URL is asking for words that describe `'ocean'`.

*Check for Understanding*: Can you put together a URL that would retrieve adjectives for the word 'baby'?
To find out if you are right, build that URL and paste it into a new request at [Postman.com](https://postman.com)!

When you feel confident that you can successfully ask for and receive a JSON object holding adjectives for any word you desire, paste the corresponding URL in a browser, hit return and view the resulting JSON object. It should look similar to the result of clicking the datamuse link above. **You will need a copy of this data for your assignment.**

## Treat JSON as a Python Dictionary

A JSON object is similar, but not the same, as a Python dictionary. While understanding the differences is beyond the scope of this class, you can explore the explanation in Canvas. Suffice it to say that the way the data is stored in memory is different. Because their structures are so similar, we can treat, in most cases, a JSON object as if it were a Python dictionary! In this activity we will do just that. 

## Your Task

Start by creating a new Python file called `pretty_json.py`.

Retrieve a JSON object from the API (as described above) by pasting the address you have composed into Postman. When composing the URL, do not add quotes or spaces. After you send the request in Postman, in the body, you should receive a list of few dictionary-like objects representing several adjectives describing the word submitted. Remember, dictionaries are structures that start and end with curly braces. In this context (return values from an API) they are properly called JSON objects.  Copy the returned JSON objects from Postman (found in the body), including the beginning and end square brackets: `[ ]` and paste the text into your Python file. Assign the text to a variable called data in this manner: 
```
data =  [{"word":"wild","score":1001},{"word":"dry","score":1000},{"word":"common","score":999}]
```
Do you see the starting and ending **curly braces** above: `{}`? Those curly braces represent the start and finish of a JSON object. As mentioned above, we will treat this structure like a Python dictionary. Do you see three sets of them? Notice each JSON Object/Python dictionary is separated by a comma. The collection of those three objects is contained within a set of square brackets, making it a list.

*Check for Understanding*: In the example code above, do you see that `'wild'` is the value given by the key `"word"` in `data[0]` ? Do you see that  `'dry'` is the value given by the key `"word"` in `data[1]` ? 

Now that you have examined the structure of a returned JSON object, it is time to put that knowledge to use! Here is your task:

Iterate over the list of dictionaries you receive from the API and extract all of the adjectives returned to you. Compose a sentence where you combine the word you submitted, together with the adjectives returned by the API, into one sentence. Each adjective should be separated by a comma.

Example output:

`Adjectives for the word Impossible:  stern, strange, old, wrong, complete, dead, great, necessary, nigh, quite, satisfactory, uniformity, first`

Learning how to access APIs and process the JSON returned is a valuable skill!

Want to explore the datamuse API to see what other functionality it provides? Check out the documentation hereLinks to an external site.. 

## Getting Started
You can access the GitHub assignment hereLinks to an external site.. Edit the file named `pretty_json.py`

# Rubric
1. The student successfully retrieves a JSON object from the API and pastes it into their Python file. (10 points) then extracts the adjectives from the JSON object and prints them in a sentence. (10 points)
3. The student successfully submits the assignment by the due date. (5 points)