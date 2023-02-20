import requests
from bs4 import BeautifulSoup
       
def pars_site(__name__):
    if __name__ == '__main__': 
        
        file_name='pars.txt'

        with open (file_name, 'w') as f:
            f.write('')
        url = 'https://rksi.ru/mobile_schedule'
        data = 'group=%C8%D1-11&stt=%CF%EE%EA%E0%E7%E0%F2%FC%21'
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'text/html; charset=windows-1251'}
        r = requests.post(url, data=data, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        classList = soup.findAll(['p', 'b'])        
        for cls in classList:
            print(cls)
            with open(file_name, "a") as file:
                print(cls, file=file)       

        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace(", ", ", ")   
        with open (file_name, 'w') as f:
            f.write(new_data)
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("  —  ", ", ")   
        with open (file_name, 'w') as f:
            f.write(new_data)
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<br/><b>", ", ") 
        with open (file_name, 'w') as f:
            f.write(new_data)
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("</b><br/>", ", ")  
        with open (file_name, 'w') as f:
            f.write(new_data)
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<p>", "") 
        with open (file_name, 'w') as f:
            f.write(new_data)
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("</p>", "")   
        with open (file_name, 'w') as f:
            f.write(new_data)
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("'Классный час</b>'", "Классный час")  
        with open (file_name, 'w') as f:
            f.write(new_data)
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("""<a href="/">На сайт</a>""", "") 
        with open (file_name, 'w') as f:
            f.write(new_data)
        # важное разделение
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<b>Информатика</b>", "") 
        with open (file_name, 'w') as f:
            f.write(new_data)        
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<b>Основы финансовой грамотности</b>", "") 
        with open (file_name, 'w') as f:
            f.write(new_data)        
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<b>Человек в современном мире</b>", "") 
        with open (file_name, 'w') as f:
            f.write(new_data)
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<b>История</b>", "") 
        with open (file_name, 'w') as f:
            f.write(new_data)        
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<b>Астрономия</b>", "") 
        with open (file_name, 'w') as f:
            f.write(new_data)        
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<b>Родной язык</b>", "") 
        with open (file_name, 'w') as f:
            f.write(new_data)
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<b>Литература</b>", "") 
        with open (file_name, 'w') as f:
            f.write(new_data)
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<b>Физика</b>", "") 
        with open (file_name, 'w') as f:
            f.write(new_data)
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<b>Физическая культура</b>", "") 
        with open (file_name, 'w') as f:
            f.write(new_data)
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<b>Математика</b>", "") 
        with open (file_name, 'w') as f:
            f.write(new_data)
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<b>Классный час</b>", "") 
        with open (file_name, 'w') as f:
            f.write(new_data)        
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<b>Большие данные</b>", "") 
        with open (file_name, 'w') as f:
            f.write(new_data)
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<b>Русский язык</b>", "") 
        with open (file_name, 'w') as f:
            f.write(new_data)
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<b>Иностранный язык</b>", "") 
        with open (file_name, 'w') as f:
            f.write(new_data)            
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<b>Экологические основы природопользования</b>", "") 
        with open (file_name, 'w') as f:
            f.write(new_data)
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<b>", "\n") 
        with open (file_name, 'w') as f:
            f.write(new_data)
        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("</b>", "") 
        with open (file_name, 'w') as f:
            f.write(new_data)

        with open (file_name, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("\n\n", "\n") 
        with open (file_name, 'w') as f:
            f.write(new_data)           
                