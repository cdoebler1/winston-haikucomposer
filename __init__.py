from mycroft import MycroftSkill, intent_file_handler
# import subprocess
import compose_haiku


class HaikuCompose(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('haiku.intent')
    def handle_haiku(self, message):
        self.speak_dialog(compose_haiku.main())

    def stop(self):
        pass


def create_skill():
    return HaikuCompose()
