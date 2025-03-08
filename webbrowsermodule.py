# enter a term, then search on the web browser

import webbrowser

user_term = input("enter the term:")

webbrowser.open("https://www.google.com/search?q=" + user_term)

