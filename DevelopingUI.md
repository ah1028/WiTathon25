# Developing the UI

To edit the UI and develop the webpages, this can be done without needing to host the website

Simply edit the HTML/CSS and view this by running the file in a web browser - double click on the html file from the file explorer

### Navigating between pages
For now, the static pages can be navigated to provided they are in the same directory as the current file

e.g. Page 1 html:
```
<!DOCTYPE html>
<html>
    <head>
        <title>Page 1</title>
    </head>
    <body>
        <h1>Page 1</h1>
        <button onclick="location.href='page2.html'">Next Page</button>
    </body>
</html>
```
Page 2 html:
```
<!DOCTYPE html>
<html>
    <head>
        <title>Page 2</title>
    </head>
    <body>
        <h1>Page 2</h1>
    </body>
</html>
```

