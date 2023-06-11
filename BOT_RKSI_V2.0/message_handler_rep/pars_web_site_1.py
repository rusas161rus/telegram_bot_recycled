import requests
from bs4 import BeautifulSoup
       
def pars_site(__name__):
    if __name__ == '__main__': 
        
        file_name='schedule.txt'
        
        url = 'https://rksi.ru/mobile_schedule'
        data = 'group=%D0%91%D0%94-11&stt=%D0%9F%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C%21'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html; charset=windows-1251'
        }
        r = requests.post(url, data=data, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        classList = soup.findAll(['p', 'b'])

        replacements = [
            (", ", ", "),
            ("  —  ", ", "),
            ("<br/><b>", ", "),
            ("</b><br/>", ", "),
            ("<p>", ""),
            ("</p>", ""),
            ("'Классный час</b>'", "Классный час"),
            ("""<a href="/">На сайт</a>""", ""),
            ("<b>Информатика</b>", ""),
            ("<b>Основы финансовой грамотности</b>", ""),
            ("<b>Человек в современном мире</b>", ""),
            ("<b>История</b>", ""),
            ("<b>Астрономия</b>", ""),
            ("<b>Родной язык</b>", ""),
            ("<b>Литература</b>", ""),
            ("<b>Физика</b>", ""),
            ("<b>Физическая культура</b>", ""),
            ("<b>Математика</b>", ""),
            ("<b>Классный час</b>", ""),
            ("<b>Большие данные</b>", ""),
            ("<b>Русский язык</b>", ""),
            ("<b>Иностранный язык</b>", ""),
            ("<b>Экологические основы природопользования</b>", ""),
            ("<b>Основы безопасности жизнедеятельности</b>", ""),
            ("<b>Социальная информатика</b>", ""),
            ("<b>География</b>", ""),
            ("<b>Экономика</b>", ""),
            ("<b>Основы банковского дела</b>", ""),
            ("<b>Обществознание</b>", ""),
            ("<b>Доп. занятие ИС-1</b>", ""),
            ("<b>", "\n"),
            ("</b>", ""),
            ("\n\n", "\n")
        ]

        with open(file_name, 'w') as f:
            for cls in classList:
                print(cls)
                print(cls, file=f)

        with open(file_name, 'r') as f:
            old_data = f.read()

        for old, new in replacements:
            old_data = old_data.replace(old, new)

        with open(file_name, 'w') as f:
            f.write(old_data)  
                
