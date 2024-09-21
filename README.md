<<<<<<< HEAD
# Bear Loves You
![bear peeking from under the table saying "i love you"](.md_img/bear.png "Bear")

## Art Credit
**Original author**: Hayley Jane Wakenshaw \
**Link**: [https://www.asciiart.eu/toys/teddy-bears](https://www.asciiart.eu/toys/teddy-bears)

## Build
```bash
make
```

## Run
```bash
./bear_loves_you
```

## Change program parameters
You can change the **color** of the different parts of the frames and the **time span** of the frames of different frame groups. The macros for all can be found in `bear.h`

### Color
Use the provided **ansi escape codes** or input your own!
```c
// Colors
#define BLUE                "\x1b[34m"
#define ANSI_COLOR_RESET    "\x1b[0m"
#define INTENSE_BROWN       "\033[38;5;130m"
#define LIGHT_GREEN         "\033[38;5;10m"
#define LIGHT_SKIN          "\033[38;5;223m"
#define MEDIUM_SKIN         "\033[38;5;137m"
#define DARK_SKIN           "\033[38;5;94m" 
#define LIGHT_PINK          "\033[38;5;217m" 
#define INTENSE_PINK        "\033[38;5;198m" 

// Parts' colors
#define BEAR_COLOR INTENSE_BROWN
#define BEAR_EYES_COLOR BLUE
#define BEAR_SKIN_COLOR MEDIUM_SKIN
#define TEXT_BUBBLE_COLOR INTENSE_PINK
#define TEXT_COLOR1 LIGHT_PINK
#define TEXT_COLOR2 INTENSE_PINK
```

The different parts are:
- `BEAR` the body of the bear
- `BEAR_EYES` the eyes of the bear
- `BEAR_SKIN` the skin of the bear's paws
- `TEXT_BUBBLE` the bear's text bubble
- `TEXT` the bubble's text

### Time Span
```c
#define TO_uSEC(s) s * 1000000
// Frame groups sleep time
#define BEAR_TIME 0.5
#define BUBBLE_TIME 0.03
#define TEXT_TIME 0.5
```
The macros refer to the usleep that happens after each frame print in `bear.c`.
```c
system("clear");
print_frame(i);
if(i<=5)        // Bear frame group
    usleep(TO_uSEC(BEAR_TIME));
else if(i<=13)  // Bubble frame group
    usleep(TO_uSEC(BUBBLE_TIME));
else            // Text frame group
    usleep(TO_uSEC(TEXT_TIME));
```
The three values can be changed so that the whole animation slows down or speeds up.

# Dedicated to Anastasia <3
=======
# basichttpserver
a basic http/1.0 server

this program acts as a HTTP/1.0 server and serves static files to clients

for now:
- [ ] follow HTTP protocol, handle headers (to the extent we need to support static web serving)
- [ ] map the paths to file system paths directly (example, "/js/a.js" translates to "a.js file from js folder", but do it safely (?) - don't give access to previous directory like "/../a.js" is invalid)
- [ ] store the file data that is sent in a hashmap or other structure in-memory so future requests won't have to read from disk each time. (Problem is of cache invalidation) 

expected to be done:
- [ ] handle folders and path etc.,
- [ ] map paths to static html files OR any other static files (css, js, and files like mp3 etc.,)

would be cool to be done:
- [ ] some sort of configuration file where could define what files would be at what paths, and other settings and start the server using CLI
- [ ] include limited server side rendering of the html files (variables declared in config file that need to be computed in runtime like, for instance, time)
- [ ] an auto-generated index HTML file that lists all the paths as hyperlinks at path '/'
- [ ] Use async/await for continuing with CPU operations (serving new requests, parsing etc) while new file reads or I/O are done in background if not in "cache" already
- [ ] some global "cache" (or a way to avoid reading from disk and using previously served/read static files) i.e. accessible to multiple processes (IPC maybe?) and if the "cache" is handled by a seperate process then if server restarts it still has access to the "cached" memory
- [ ] another process that uses OS file change notifier or any other way(s) to check if the file has beend updated or modified, then get the difference to the one already in cache and modify it in cache by applying the difference

## log
so we need a way to handle HTTP/1.0 Requests and Responses according to the <https://datatracker.ietf.org/doc/html/rfc1945>
>>>>>>> 5c3b4d36ddbbe324ba602c2d88a33d1f79a50138
