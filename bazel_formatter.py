import os
import subprocess

import sublime_plugin


class BazelFormatterCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        filename = self.view.file_name()
        # TODO: Better handle installation directory of buildifier and go/bin PATH.
        ret = subprocess.run(['buildifier', filename], capture_output=True)
        if ret.returncode != 0:
            self.view.window().status_message('Failed to run buildifier on ' + filename +
                                              '\nError: ' + ret.stdout)
        else:
            self.view.window().status_message('Formatted ' + filename)
