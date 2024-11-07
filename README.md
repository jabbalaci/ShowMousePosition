Show Mouse Position
===================

A little GUI tool that shows the current mouse position, i.e. the X any Y coordinates
of your mouse pointer. The coordinates are updated as you move the mouse.

Motivation
----------

I made this tool to facilitate work with [pyautogui](https://github.com/asweigart/pyautogui).

Screenshots
-----------

![](assets/01.jpg)

![](assets/02.png)

The idea is to let it run in a corner and read the mouse coordinates when needed.

Usage
-----

Start it in a terminal because it can print the mouse coordinates
to the standard output.

The program has the following shortcuts:

```
Ctrl+H                    this help
Ctrl+Q                    quit
Ctrl+P                    print mouse coordinates on stdout
Ctrl+S, Ctrl+-            print separator on stdout
Ctrl+Enter                print a new line on stdout
Ctrl+L                    clear screen
Ctrl+C                    copy mouse coordinates to clipboard
```

Supported Platforms
-------------------

I tried it under Linux and Windows, but it should also work on macOS.

Links
-----

* [reddit discussion](https://old.reddit.com/r/Python/comments/zc7ldk/i_made_a_little_gui_tool_that_shows_the_current/)
