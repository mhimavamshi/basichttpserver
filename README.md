# basichttpserver
a basic http/1.0 server

this program acts as a HTTP/1.0 server and serves static files to clients

for now:
- [X] follow HTTP protocol, handle headers (to the extent we need to support static web serving)
- [X] map the paths to file system paths directly (example, "/js/a.js" translates to "a.js file from js folder")
- [X] python program to generate index.html with hyperlinks to all files in the directory, at the moment it runs
- [X] path '/' points to index.html exclusively or redirects
- [X] Handle images and other data
- [ ] Error Handling
- [ ] Use HTTP/1.0 caching mechanism
    - [X] Added "Expires" header
    - [X] Added "Last-Modified" header
- [ ] Handle Encoding
- [X] store the file data that is sent in a hashmap or other structure in-memory so future requests won't have to read from disk each time. (Problem is of "cache" invalidation) 
- [ ] stop using threads (due to GIL etc.,) and use async await

expected to be done:
- [ ] handle folders and path etc.,
- [ ] map paths to static html files OR any other static files (css, js, and files like mp3 etc.,)

would be cool to be done:
- [ ] some sort of configuration file where could define what files would be at what paths, and other settings and start the server using CLI
- [ ] include limited server side rendering of the html files (variables declared in config file that need to be computed in runtime like, for instance, time)
- [ ] an auto-generated index HTML file that lists all the paths as hyperlinks at path '/', at runtime
- [ ] Use async/await for continuing with CPU operations (serving new requests, parsing etc) while new file reads or I/O are done in background if not in "cache" already
- [ ] some global "cache" (or a way to avoid reading from disk and using previously served/read static files) i.e. accessible to multiple processes (IPC maybe?) and if the "cache" is handled by a seperate process then if server restarts it still has access to the "cached" memory
- [ ] another process that uses OS file change notifier or any other way(s) to check if the file has been updated or modified, then get the difference to the one already in cache and modify it in cache by applying the difference

## Usage
for testing purpose:
```
$ python test.py
```
and view in your choice of web browser at the specified host and port (default is 5000) 

## log
so we need a way to handle HTTP/1.0 Requests and Responses according to the <https://datatracker.ietf.org/doc/html/rfc1945>
