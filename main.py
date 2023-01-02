from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import TouchBehavior, MagicBehavior

class MyButton(MDIconButton, TouchBehavior, MagicBehavior):
    save = ''

    def __init__(self, sym, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sym = sym

    def on_release(self):
        super().on_release()
        tt = ''
        t = calc.lab[-1].text
        if len(calc.lab) == 2:
            tt = calc.lab[-2].text
        if tt == '365-311=54':
            calc.lab[-2].text = 'Вітаю, ти знайшов першу пасхалку!'
            calc.lab[-2].theme_text_color = "Custom"
            calc.lab[-2].text_color = '#ff0000'
            calc.lab[-2].on_text_color(calc.lab[-2], '#ff0000')
        if len(t) > 1 and t[0] == '0':
            t = t[1:]
        if t == 'На нуль ділити не можна':
            t = ''
        if self.sym in '1234567890':
            if MyButton.save == '':
                calc.lab[-1].text = t + self.sym
            elif MyButton.save == t:
                calc.lab[-1].text = self.sym
            else:
                calc.lab[-1].text = t + self.sym
        elif self.sym in '*/+-' and t != '':
            if MyButton.save == '':
                calc.lab[-1].text = t + self.sym
                MyButton.save = t + self.sym
            else:
                if ('+' or '-' or '/' or '*') == MyButton.save[-1]:
                    calc.lab[-1].text = t[:-1] + self.sym
                    MyButton.save = t[:-1] + self.sym
                else:
                    calc.lab.append(MDLabel(bold=True, pos_hint={"center_x": 0.2, "center_y": 0.2}))
                    calc.bl.add_widget(calc.lab[-1])
                    calc.lab[-2].bold = False
                    try:
                        calc.lab[-2].text = MyButton.save + t + '=' + str(eval(MyButton.save + t))
                        calc.lab[-1].text = str(eval(MyButton.save + t)) + self.sym
                    except ZeroDivisionError:
                        calc.lab[-1].text = 'На нуль ділити не можна'
                    t = MyButton.save = ''
        elif self.sym == '=' and t != '':
            try:
                tt = str(eval(MyButton.save + t))
                calc.lab[-1].text = tt
                MyButton.save = MyButton.save + t + '=' + tt
                calc.lab.append(MDLabel(bold=True, pos_hint={"center_x": 0.2, "center_y": 0.2}))
                calc.bl.add_widget(calc.lab[-1])
                calc.lab[-2].bold = False
                calc.lab[-2].text = MyButton.save
                t = MyButton.save = ''
            except ZeroDivisionError:
                calc.lab[-1].text = 'На нуль ділити не можна'
        elif self.sym == 'C':
            calc.lab[-1].text = t[:-1]

class CalculatorApp(MDApp):
    lab = []

    def build(self):
        bll = MDBoxLayout(orientation = 'vertical')
        gl = MDGridLayout(
            spacing = "20dp",
            adaptive_size = True,
            padding = 20,
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
            rows = 4,
            cols = 4
            )
        self.bl = MDBoxLayout(
            pos_hint = {"center_x": 0.9, "center_y": 0.3},
            orientation = 'vertical'
        )
        self.lab.append(MDLabel(bold = True, pos_hint = {"center_x": 0.2, "center_y": 0.2}))
        btn1 = MyButton(sym = '1', icon = "Images/a1.png", md_bg_color = "#ffffff")
        btn2 = MyButton(sym = '2', icon = "Images/a2.png", md_bg_color = "#ffffff")
        btn3 = MyButton(sym = '3', icon = "Images/a3.png", md_bg_color = "#ffffff")
        btn4 = MyButton(sym = '4', icon = "Images/a4.png", md_bg_color = "#ffffff")
        btn5 = MyButton(sym = '5', icon = "Images/a5.png", md_bg_color = "#ffffff")
        btn6 = MyButton(sym = '6', icon = "Images/a6.png", md_bg_color = "#ffffff")
        btn7 = MyButton(sym = '7', icon = "Images/a7.png", md_bg_color = "#ffffff")
        btn8 = MyButton(sym = '8', icon = "Images/a8.png", md_bg_color = "#ffffff")
        btn9 = MyButton(sym = '9', icon = "Images/a9.png", md_bg_color = "#ffffff")
        btn0 = MyButton(sym = '0', icon = "Images/a0.png", md_bg_color = "#ffffff")
        btnm = MyButton(sym = '-', icon = "Images/a-.png", md_bg_color = "#ffffff")
        btnd = MyButton(sym = '+', icon = "Images/a+.png", md_bg_color = "#ffffff")
        btnr = MyButton(sym = '=', icon = "Images/a=.png", md_bg_color = "#ffffff")
        btnp = MyButton(sym = '/', icon = "Images/a'.png", md_bg_color = "#ffffff")
        btnx = MyButton(sym = '*', icon = "Images/ax.png", md_bg_color = "#ffffff")
        btnc = MyButton(sym = 'C', icon = "Images/ac.png", md_bg_color = "#ffffff")
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
        self.bl.add_widget(self.lab[0])
        bll.add_widget(self.bl)
        bll.add_widget(gl)
        return (
            MDScreen(
                bll
            )
        )

calc = CalculatorApp()
calc.run()