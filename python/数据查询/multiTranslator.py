import googletrans
import baidu_translate
import youdao_translate

class Translator:
    def __init__(self):
        self.translators = [googletrans.Translator(), baidu_translate.Translator(), youdao_translate.Translator()]
        self.current_translator = self.translators[0]
        self.max_errors = 3
        self.current_errors = 0

    def translate(self, text, target_lang):
        try:
            result = self.current_translator.translate(text, target_lang)
            return result
        except Exception as e:
            print(e)
            self.current_errors += 1
            if self.current_errors >= self.max_errors:
                self.switch()
            return None

    def switch(self):
        self.current_errors = 0
        current_index = self.translators.index(self.current_translator)
        next_index = (current_index + 1) % len(self.translators)
        self.current_translator = self.translators[next_index]