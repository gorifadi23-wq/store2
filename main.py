from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

from excel_reader import read_excel_file

Window.size = (400, 700)

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.label = Label(text="اختر ملف Excel لتحويله إلى نظام إدارة")
        self.add_widget(self.label)

        btn = Button(text="اختيار ملف Excel")
        btn.bind(on_press=self.load_excel)
        self.add_widget(btn)

        self.result_area = ScrollView(size_hint=(1, 1))
        self.result_grid = GridLayout(cols=1, size_hint_y=None)
        self.result_grid.bind(minimum_height=self.result_grid.setter('height'))
        self.result_area.add_widget(self.result_grid)
        self.add_widget(self.result_area)

    def load_excel(self, instance):
        # مسار ثابت مؤقتاً – لاحقاً نضيف اختيار ملف
        path = "data.xlsx"

        try:
            data = read_excel_file(path)
            self.result_grid.clear_widgets()

            for row in data:
                self.result_grid.add_widget(Label(text=str(row)))
            
            self.label.text = "تم تحميل الملف بنجاح"

        except Exception as e:
            self.label.text = f"خطأ: {e}"

class ExcelManagerApp(App):
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    ExcelManagerApp().run()
