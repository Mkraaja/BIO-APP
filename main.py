from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatIconButton, MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivy.core.window import Window

# Set window size for testing on PC (matches phone aspect ratio)
Window.size = (360, 640)

KV = '''
MDScreen:
    md_bg_color: 1, 1, 1, 1

    MDBoxLayout:
        orientation: 'vertical'
        padding: "20dp"
        spacing: "15dp"

        MDLabel:
            text: "BIOSECURITY PRO"
            halign: "center"
            font_style: "H5"
            theme_text_color: "Custom"
            text_color: 0, 0.62, 0.38, 1 # Shamrock Green
            bold: True

        MDTextField:
            id: length
            hint_text: "Length (ft)"
            mode: "rectangle"
            input_filter: "float"

        MDTextField:
            id: width
            hint_text: "Width (ft)"
            mode: "rectangle"
            input_filter: "float"

        MDRaisedButton:
            text: "CALCULATE WET PROCESS"
            pos_hint: {"center_x": .5}
            md_bg_color: 0, 0.62, 0.38, 1
            on_release: app.calculate()

        MDCard:
            size_hint: 1, None
            height: "180dp"
            elevation: 2
            padding: "15dp"
            md_bg_color: 0.95, 0.95, 0.95, 1

            MDLabel:
                id: result_label
                text: "Results will appear here"
                halign: "center"
                theme_text_color: "Secondary"
'''

class BiosecurityApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

    def format_val(self, val):
        if val < 1:
            return f"{int(val * 1000)} ml"
        return f"{val:.2f} L"

    def calculate(self):
        try:
            l = float(self.root.ids.length.text)
            w = float(self.root.ids.width.text)
            
            # Use your Schippers/Traineeship logic here
            area_sqm = (l * w) / 10.7639
            vol = area_sqm * 0.56
            
            alk_qty = vol * 0.02 # Example 2% dose
            
            res = f"Area: {l*w:.1f} sq.ft\\n"
            res += f"Mix {self.format_val(alk_qty)} Cleaner\\n"
            res += f"with {self.format_val(vol - alk_qty)} Water"
            
            self.root.ids.result_label.text = res
            self.root.ids.result_label.theme_text_color = "Primary"
        except:
            self.root.ids.result_label.text = "Error: Enter valid numbers"

BiosecurityApp().run()
