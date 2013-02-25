import sublime
import sublime_plugin
import tempfile

class BuildSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # run command for each selection
        for region in self.view.sel():
            content = ""
            if region.empty():
                # if nothing is selected, then use entire file contents
                region = sublime.Region(0, self.view.size())
                content = self.view.substr(region)
            else:
                # Get the selected text  
                content = self.view.substr(region)

            self.build(content)


    def build(self, content = ""):
        # ignore empty contents
        if len(content) == 0:
            return

        # create temporary file
        tmp_file = tempfile.NamedTemporaryFile(delete=False)
        tmp_file.write(content)
        tmp_file.close()
        # get settings (same as build system uses)
        setting = sublime.load_settings("BuildSelection.sublime-settings")
        cmd_list = setting.get("cmd")
        file_regex = setting.get("file_regex", "")
        line_regex = setting.get("line_regex", "")
        working_dir = setting.get("working_dir", "")
        encoding = setting.get("encoding", "utf-8")
        env = setting.get("env", {})
        shell = setting.get("shell", True)
        path = setting.get("path", "")

        # construct exec command from list (replace $file with temp file)
        cmd = self.replace_args1(cmd_list, tmp_file.name)

        # print "executing command..."
        # run da command!
        self.view.window().run_command("exec", {
            "cmd": cmd,
            "file_regex": file_regex,
            "line_regex": line_regex,
            "working_dir": working_dir,
            "encoding": encoding,
            "env": env,
            "shell": shell,
            "path": path
        })
        # TODO: cleanup, delete the file ?


    def replace_args1(self, cmd_list, filename):
        for i,cmd in enumerate(cmd_list):
            cmd_list[i] = cmd.replace("$file", filename)
        cmd = " ".join(cmd_list)
        return cmd


""" for testing:
    SELECT 1 as col1
           ,1d as col2
"""
