String Highlighter-
This app is to highlight a slice of a string in the provided start and end
image.png

To execute the code just go into folder string_highlighter where you'll find the manage.py and execute the following command:
> python manage.py runserver

It will prompt the url, open it in browser

Validation scenarios handled:
1. if any input box is empty
2. if start and end is numeric values
3. if start and end is a non negative number
4. if start is not greater than end
5. if end is not greater then length of the string