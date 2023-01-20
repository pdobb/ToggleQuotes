import sublime
import sublime_plugin

class ToggleQuotesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                region = self.view.line(region)

            if not region.empty():
                current_text = self.view.substr(region)

                new_text = self._toggle_quotes(current_text)

                if new_text != current_text:
                    self.view.replace(edit, region, new_text)

    @staticmethod
    def _toggle_quotes(text):
        return text.translate(str.maketrans("'\"", "\"'"))
