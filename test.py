import wikipedia

article_title = "Python (programming language)"
article_page = wikipedia.page(article_title)
# Now you can access various attributes of the page, such as content, summary, etc.
print(article_page.section)