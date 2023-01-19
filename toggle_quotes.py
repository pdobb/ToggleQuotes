import sublime
import sublime_plugin

def _toggle_quotes(text):
    return text.translate(str.maketrans("'\"", "\"'"))

class ToggleQuotesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                region = self.view.line(region)

            if not region.empty():
                current_text = self.view.substr(region)

                new_text = _toggle_quotes(current_text)

                if new_text != current_text:
                    self.view.replace(edit, region, new_text)
