Sublime-Coffeelint
----------------

A very bare-bones coffeelint plugin for Sublime Text 2 & 3 on OS X or Linux.
It simply runs `coffeelint` when you save a `.coffee` file, and prints the output to the console.

### Requirements:

Install coffeelint: `npm install -g coffeelint`

You should have `/usr/local/bin/node` and /usr/local/bin/coffeelint`

### Manual Installation

Copy these files to `~/Library/Application Support/Sublime Text 2/Packages/Coffeelint`


### How to use

Set the build system to coffeelint, and then select the "Build" command (Tools > Build System > coffeelint).

Alternatively, just save a `.coffee` file and it should run automatically.

