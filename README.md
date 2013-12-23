BuildSelection
==============

BuildSelection is a Sublime Text 2/3 plugin to pass current selection to external command.
It will utilize standard Sublime Text build system, but placeholder $file will point to a temporary file(s) with contents of your current selection(s).
To configure create BuildSelection.sublime-settings file with settings indentical to one that are used for built-in sublime build system.

NOTE:
  Build settings file_regex and line_regex cannot be used to point to error as line numbers in original file and temporary files do not match

Example configuration for running PostgreSQL psql client:
```json
{
    "cmd": ["psql", "-U", "USER_NAME", "-d", "DATABASE", "-f", "$file"],
    "path": "C:/Program Files (x86)/pgAdmin III/1.18/"
    // "line_regex": "^LINE\\s+([0-9]+):"
    // "file_regex": "",
    // "working_dir": "",
    // "encoding": "",
    // "env": "",
    // "shell": ""
}
```

To register keymap for quick selection building use menu:
Preferences -> Key Bindings - User

Add a line like this one:
```json
    { "keys": ["ctrl+e"], "command": "build_selection" }
```
