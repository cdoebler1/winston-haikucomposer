from mycroft import MycroftSkill, intent_file_handler
# import subprocess
from .compose_haiku import generatehaiku as genHaiku


class HaikuCompose(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('haiku.intent')
    def handle_haiku(self, message):
        Haiku = genHaiku()
        line1 = (' '.join(Haiku[0]))
        line2 = (' '.join(Haiku[1]))
        line3 = (' '.join(Haiku[2]))
        self.speak_dialog(line1)
        self.speak_dialog(line2)
        self.speak_dialog(line3)

    def stop(self):
        pass


def create_skill():
    return HaikuCompose()
