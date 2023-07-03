from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from plyer import notification


class PomodoroApp(App):
    pomodoro_time = 25 * 60
    short_break_time = 5 * 60
    long_break_time = 35 * 60
    current_time = 0

    def build(self):
        layout = BoxLayout(orientation="vertical")

        top_third = BoxLayout(orientation="vertical")
        middle_third = BoxLayout(orientation="vertical")
        bottom_third = BoxLayout(orientation="vertical")

        layout.add_widget(top_third)
        layout.add_widget(middle_third)
        layout.add_widget(bottom_third)

        self.app_label = Label(text="Simple Pomodoro App")
        top_third.add_widget(self.app_label)

        self.pomo_button = Button(text="Pomodoro")
        top_third.add_widget(self.pomo_button)

        self.short_break_button = Button(text="Short Break")
        middle_third.add_widget(self.short_break_button)

        self.long_break_button = Button(text="Long Break")
        bottom_third.add_widget(self.long_break_button)

        self.pomo_button.bind(on_release=self.start_pomodoro)
        self.short_break_button.bind(on_release=self.start_short_break)
        self.long_break_button.bind(on_release=self.start_long_break)

        Clock.schedule_interval(self.update_timer, 1)
        return layout

    def start_pomodoro(self, instance):
        self.app_label.text = "Starting Pomodoro"
        self.current_time = self.pomodoro_time

    def start_short_break(self, instance):
        self.app_label.text = "Starting Short Break"
        self.current_time = self.short_break_time

    def start_long_break(self, instance):
        self.app_label.text = "Starting Long Break"
        self.current_time = self.long_break_time

    def update_timer(self, dt):
        if self.current_time > 0:
            self.current_time -= 1
            minutes = self.current_time // 60
            seconds = self.current_time % 60
            self.app_label.text = f"{minutes:02d}:{seconds:02d}"

            if self.current_time == 0:
                self.schedule_notification(f"{self.app_label.text} Finished!")

    def schedule_notification(self, message):
        notification.notify(
            title="SimplePomodoro App",
            message=message,
            timeout=10,
        )


if __name__ == "__main__":
    PomodoroApp().run()
