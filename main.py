from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.behaviors import TouchBehavior, MagicBehavior

class MyButton(MDIconButton, TouchBehavior, MagicBehavior):
    save = ''

    def __init__(self, sym, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sym = sym

    def on_release(self):
        super().on_release()
        t = calc.textfield.text
        if self.sym in '1234567890':
            if MyButton.save == '':
                calc.textfield.set_text(calc.textfield, t + self.sym)
            else:
                calc.textfield.set_text(calc.textfield, self.sym)
        elif self.sym in '*/+-':
            calc.textfield.set_text(calc.textfield, t + self.sym)
            MyButton.save = t + self.sym
        elif self.sym == '=':
            try:
                tt = str(eval(MyButton.save + t))
                calc.textfield.set_text(calc.textfield, tt)
            except ZeroDivisionError:
                calc.textfield.set_text(calc.textfield, 'На нуль ділити не можна')
        elif self.sym == 'C':
            calc.textfield.set_text(calc.textfield, t[:-1])

class CalculatorApp(MDApp):
    def build(self):
        gl = MDGridLayout(
                    spacing = "56dp",
                    adaptive_size = True,
                    pos_hint = {"center_x": 0.5, "center_y": 0.5},
                    rows = 5,
                    cols = 5
                )
        btn1 = MyButton(sym = '1', icon = "Images\\a1.png", md_bg_color = "#ffffff")
        btn2 = MyButton(sym = '2', icon = "Images\\a2.png", md_bg_color = "#ffffff")
        btn3 = MyButton(sym = '3', icon = "Images\\a3.png", md_bg_color = "#ffffff")
        btn4 = MyButton(sym = '4', icon = "Images\\a4.png", md_bg_color = "#ffffff")
        btn5 = MyButton(sym = '5', icon = "Images\\a5.png", md_bg_color = "#ffffff")
        btn6 = MyButton(sym = '6', icon = "Images\\a6.png", md_bg_color = "#ffffff")
        btn7 = MyButton(sym = '7', icon = "Images\\a7.png", md_bg_color = "#ffffff")
        btn8 = MyButton(sym = '8', icon = "Images\\a8.png", md_bg_color = "#ffffff")
        btn9 = MyButton(sym = '9', icon = "Images\\a9.png", md_bg_color = "#ffffff")
        btn0 = MyButton(sym = '0', icon = "Images\\a0.png", md_bg_color = "#ffffff")
        btnm = MyButton(sym = '-', icon = "Images\\a-.png", md_bg_color = "#ffffff")
        btnd = MyButton(sym = '+', icon = "Images\\a+.png", md_bg_color = "#ffffff")
        btnr = MyButton(sym = '=', icon = "Images\\a=.png", md_bg_color = "#ffffff")
        btnp = MyButton(sym = '/', icon = "Images\\a'.png", md_bg_color = "#ffffff")
        btnx = MyButton(sym = '*', icon = "Images\\ax.png", md_bg_color = "#ffffff")
        btnc = MyButton(sym = 'C', icon = "Images\\ac.png", md_bg_color = "#ffffff")
        gl.add_widget(btn1)
        gl.add_widget(btn2)
        gl.add_widget(btn3)
        gl.add_widget(btn4)
        gl.add_widget(btn5)
        gl.add_widget(btn6)
        gl.add_widget(btn7)
        gl.add_widget(btn8)
        gl.add_widget(btn9)
        gl.add_widget(btn0)
        gl.add_widget(btnm)
        gl.add_widget(btnd)
        gl.add_widget(btnr)
        gl.add_widget(btnp)
        gl.add_widget(btnx)
        gl.add_widget(btnc)
        self.textfield = MDTextField(
                    mode = 'rectangle',
                    pos_hint = {"center_x": 0.5, "center_y": 0.95}
                )
        self.theme_cls.primary_palette = "Orange"
        return (
            MDScreen(
                self.textfield,
                gl
            )
        )

calc = CalculatorApp()
calc.run()