import os
import subprocess

import sublime_plugin


class BazelFormatterCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        filename = self.view.file_name()
        ret = subprocess.run(['/home/heethesh/go/bin/buildifier', filename], capture_output=True)
        if ret.returncode != 0:
            self.view.window().status_message('Failed to run buildifier on ' + filename +
                                              '\nError: ' + ret.stdout)
        else:
            self.view.window().status_message('Formatted ' + filename)
