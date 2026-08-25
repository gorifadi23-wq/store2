from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.card import MDCard
from kivymd.uix.gridlayout import MDGridLayout

from plyer import filechooser
from excel_reader import read_excel_file


class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = MDBoxLayout(orientation="vertical", spacing=20, padding=20)
        self.add_widget(self.layout)

        # عنوان التطبيق
        self.title = MDLabel(
            text="📊 مدير ملفات Excel الذكي",
            halign="center",
            theme_text_color="Primary",
            font_style="H5"
        )
        self.layout.add_widget(self.title)

        # زر اختيار ملف
        self.btn = MDRectangleFlatIconButton(
            text="اختيار ملف Excel",
            icon="file-excel",
            pos_hint={"center_x": 0.5},
            on_release=self.open_file_picker
        )
        self.layout.add_widget(self.btn)

        # منطقة عرض النتائج
        self.scroll = MDScrollView()
        self.grid = MDGridLayout(cols=1, adaptive_height=True, spacing=10, padding=10)
        self.scroll.add_widget(self.grid)
        self.layout.add_widget(self.scroll)

    def open_file_picker(self, instance):
        filechooser.open_file(on_selection=self.load_excel)

    def load_excel(self, selection):
        if not selection:
            self.title.text = "❌ لم يتم اختيار أي ملف"
            return

        path = selection[0]
        self.title.text = f"📁 جاري قراءة الملف:\n{path}"

        try:
            data = read_excel_file(path)
            self.grid.clear_widgets()

            for row in data:
                card = MDCard(
                    orientation="vertical",
                    padding=15,
                    size_hint=(1, None),
                    height=120,
                    md_bg_color=(0.95, 0.95, 0.95, 1),
                    radius=[15]
                )
                card.add_widget(MDLabel(text=str(row), halign="left"))
                self.grid.add_widget(card)

            self.title.text = "✔ تم تحميل الملف بنجاح"

        except Exception as e:
            self.title.text = f"⚠ خطأ أثناء قراءة الملف:\n{e}"


class ExcelManagerApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return MainScreen()


if __name__ == "__main__":
    ExcelManagerApp().run()
