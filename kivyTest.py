# import kivy
# from kivymd.app import MDApp
# from kivymd.uix.screen import Screen
# from kivymd.uix.textfield import MDTextField
#
# kivy.require('1.10.0')
#
# from kivy.app import App
# from kivy.uix.button import Label
#
#
# # Inherit Kivy's App class which represents the window
# # for our widgets
# # HelloKivy inherits all the fields and methods
# # from Kivy
#
#
# class HelloKivy(MDApp):
#
#     # This returns the content we want in the window
#     def build(self):
#         screen = Screen()
#         username = MDTextField(text='Enter Your Name', pos_hint={'center_x': 0.5, 'center_y': 0.5},)
#         screen.add_widget(username)
#         return screen
#
#
# HelloKivy().run()


from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
BoxLayout:
    padding: "10dp"

    MDTextField:
        id: text_field_error
        hint_text: "Enter the value"
        helper_text: "Error May Occur"
        helper_text_mode: "on_error"
        pos_hint: {"center_y": .5}
'''


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        self.screen.ids.text_field_error.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        return self.screen

    def set_error_message(self, instance_textfield):
        self.screen.ids.text_field_error.error = True


Test().run()