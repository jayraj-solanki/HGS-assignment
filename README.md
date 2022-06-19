String Highlighter-
This app is to highlight a slice of a string in the provided input, start and end
![image](https://user-images.githubusercontent.com/25260417/174498957-3f03c985-0b3a-4268-ac4c-5cb07a812a6a.png)


To execute the code just go into folder string_highlighter where you'll find the manage.py and execute the following command:
> python manage.py runserver

It will prompt the url, open it in browser

Validation scenarios handled:
1. if any input box is empty
2. if start and end is numeric values
3. if start and end is a non negative number
4. if start is not greater than end
5. if end is not greater then length of the string
