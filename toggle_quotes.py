import sublime
import sublime_plugin

def _toggle_quotes(text):
    new_chars = []

    for char in list(text):
        if char == "'":
            new_chars.append('"')
        elif char == '"':
            new_chars.append("'")
        else:
            new_chars.append(char)

    return "".join(new_chars)

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
