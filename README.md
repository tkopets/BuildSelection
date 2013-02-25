BuildSelection
==============

BuildSelection is a Sublime Text plugin to pass current selection to external command.
To configure create BuildSelection.sublime-settings file with settings indentical to one that are used for built-in sublime build system.

Example configuration for running PostgreSQL psql client:
```json
{
	"cmd": ["psql", "-U", "USER_NAME", "-d", "DATABASE", "-f", "$file"],
    "line_regex": "^LINE\\s+([0-9]+):"
    // "file_regex": "",
    // "working_dir": "",
    // "encoding": "",
    // "env": "",
    // "shell": "",
    // "path": ""
}
```