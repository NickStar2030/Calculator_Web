from flet import *

def main(page:Page):
    
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    def show(value):
        Label_result.value += value
        Label_result.update()
        
    def clear():
        Label_result.value = ""
        Label_result.update()
    def delete():
        Label_result.value = Label_result.value[:-1]
        Label_result.update()
    def calculate():
        try:
            result=""
            result=str(eval(Label_result.value))
            Label_result.value = result   
        except:
            Label_result.value = ""
            Label_result.value = "Error"
        Label_result.update()
    Label_result = TextField(bgcolor='#1b2631',color='#a0cafd',width=330)
    r1 = Row([
        ElevatedButton(text='AC',bgcolor='#1b2631',width=75,height=50,on_click=lambda _: clear()),
        ElevatedButton(text="←",bgcolor='#1b2631',width=75,height=50,on_click=lambda _: delete()),
        ElevatedButton(text='%',bgcolor='#1b2631',width=75,height=50,on_click=lambda _: show('%')),
        ElevatedButton(text='÷',bgcolor='#1b2631',width=75,height=50,on_click=lambda _: show('/')),
        
    ],alignment=MainAxisAlignment.CENTER)
    r2 = Row([
        ElevatedButton(text='7',bgcolor='#1b2631',width=75,height=50,on_click=lambda _: show('7')),
        ElevatedButton(text='8',bgcolor='#1b2631',width=75,height=50,on_click=lambda _: show('8')),
        ElevatedButton(text='9',bgcolor='#1b2631',width=75,height=50,on_click=lambda _: show('9')),
        ElevatedButton(text='×',bgcolor='#1b2631',width=75,height=50,on_click=lambda _: show('*')),        
    ],alignment=MainAxisAlignment.CENTER)
    r3 = Row([
        ElevatedButton(text='4',bgcolor='#1b2631',width=75,height=50,on_click=lambda _: show('4')),
        ElevatedButton(text='5',bgcolor='#1b2631',width=75,height=50,on_click=lambda _: show('5')),
        ElevatedButton(text='6',bgcolor='#1b2631',width=75,height=50,on_click=lambda _: show('6')),
        ElevatedButton(text='-',bgcolor='#1b2631',width=75,height=50,on_click=lambda _: show('-')),
    ],alignment=MainAxisAlignment.CENTER)
    r4 = Row([
        ElevatedButton(text='1',bgcolor='#1b2631',width=75,height=50,on_click=lambda _: show('1')),
        ElevatedButton(text='2',bgcolor='#1b2631',width=75,height=50,on_click=lambda _: show('2')),
        ElevatedButton(text='3',bgcolor='#1b2631',width=75,height=50,on_click=lambda _: show('3')),
        ElevatedButton(text='+',bgcolor='#1b2631',width=75,height=50,on_click=lambda _: show('+')),
    ],alignment=MainAxisAlignment.CENTER)
    r5 = Row([
        ElevatedButton(text='0',bgcolor='#1b2631',width=75,height=50,on_click=lambda _: show('0')),
        ElevatedButton(text='.',bgcolor='#1b2631',width=75,height=50,on_click=lambda _: show('.')),
        ElevatedButton(text='=',bgcolor='#1b2631',width=75,height=50,on_click=lambda _: calculate()),

    ],alignment=MainAxisAlignment.CENTER)
    page.add(Label_result,r1,r2,r3,r4,r5)
    page.update()

app(main,view=AppView.WEB_BROWSER)
