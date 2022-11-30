#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

fileitem = form["filename"]

# Test if the file was uploaded
if fileitem.filename:

    # strip leading path from file name
    # to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open(fn, 'wb').write(fileitem.file.read())
    message = 'The file "' + fn + '" was uploaded successfully'

else:
    message = 'No file was uploaded'

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Test Form (UPLOAD) Result</title>")
print ("<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">")
print ("<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>")
print ("<link href=\"https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap\" rel=\"stylesheet\">")
print ("<style>")
print ("body {font-family: 'Fredoka One';}")
print ("</style>")
print ("</head>")
print ("<body>")
print ("<h2>Test Form (UPLOAD) Result</h2>")
# print ("<div>%s</div>" %(fileitem))
print ("<h3>%s</h3>" %(message))
# print ("<img src=\"" + fn + "\">")
print("<a href=\"/form-test.html\"> * go to from test</a>")
print ("</body>")
print ("</html>")