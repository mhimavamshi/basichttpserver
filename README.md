# basichttpserver
a basic http server

this program acts as a HTTP server and serves a static html file to the client at a route

for now:
- index.html at route '/' for HTTP GET request

expected to be done:
- map paths to static html files OR any other static files (css, js, and files like mp3 etc.,)

would be cool to be done:
- include server side rendering of the html files


## log
so we need a way to handle HTTP Requests and Responses according to the <https://www.rfc-editor.org/rfc/rfc9110.html>
and afaik as of now, to improve efficiency we can cache the HTML body and/or preload the HTML files, and handle the HTTP requests using multiprocessing OR use async await for the I/O operation of reading the files and then serve the HTTP responses when idle i.e. CPU operations. IF the latter's done then cache the files, in memory to avoid reading from disks, for future requests.