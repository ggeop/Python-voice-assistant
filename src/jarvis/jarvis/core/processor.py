from jarvis.actions import Actions
from jarvis.utils.application_utils import start_up
from jarvis.utils.wolframalpha_util import call_wolframalpha


class Processor:
    def __init__(self):
        self.action_controller = Actions()

    def run(self):
        start_up()
        while True:
            self._process()

    def _process(self):
        # Check if the assistant is waked up
        if self.action_controller.wake_up_check():
            # Record user voice and create a voice transcipt
            self.action_controller.get_transcript()

            # Extract actions and update the actions (state of action controller)
            self.action_controller.get_skills()

            # Checks is there is an action to execute them
            if self.action_controller.skills_to_execute:
                self.action_controller.execute()
            else:
                # Check for shutdown
                self.action_controller.shutdown_check()

                # If there is not an action the assistant make a request in
                # WolframAlpha api for response
                call_wolframalpha(self.action_controller.latest_voice_transcript)

        # Check for shutdown
        self.action_controller.shutdown_check()