from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.metrics import dp

# إعدادات النظام
Window.size = (850, 500)

class SecureHubApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        sm = MDScreenManager()
        sm.add_widget(TermsScreen(name='terms'))
        sm.add_widget(AuthScreen(name='auth'))
        return sm

class TermsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=dp(20))
        layout.add_widget(MDLabel(text="سياسة الاستخدام", halign="center", font_style="H4"))
        # إضافة مربع الموافقة
        self.chk = MDCheckbox(size_hint=(None, None))
        layout.add_widget(self.chk)
        btn = MDRaisedButton(text="موافق", on_release=lambda x: setattr(self.manager, 'current', 'auth') if self.chk.active else None)
        layout.add_widget(btn)
        self.add_widget(layout)

class AuthScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        self.input = MDTextField(hint_text="أدخل كود شيما أو كلمة السر", password=True)
        layout.add_widget(self.input)
        
        self.change_btn = MDRaisedButton(text="تغيير كلمة السر", on_release=self.change_pass)
        layout.add_widget(self.change_btn)
        
        btn = MDRaisedButton(text="دخول", on_release=self.verify)
        layout.add_widget(btn)
        self.add_widget(layout)

    def verify(self, instance):
        # هنا يتم التحقق من المدخلات
        pass

    def change_pass(self, instance):
        # منطق تغيير كلمة السر
        pass

if __name__ == "__main__":
    SecureHubApp().run()
