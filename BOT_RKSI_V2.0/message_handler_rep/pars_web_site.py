import requests
from bs4 import BeautifulSoup
       
def pars_site(__name__):
    if __name__ == '__main__':
        with open ('pars.txt', 'w') as f:
            f.write('')
        url = 'https://rksi.ru/mobile_schedule'
        data = 'group=%C8%D1-11&stt=%CF%EE%EA%E0%E7%E0%F2%FC%21'
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'text/html; charset=windows-1251'}
        r = requests.post(url, data=data, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        classList = soup.findAll('p')
        for cls in classList:
            print(cls)
            with open("pars.txt", "a") as file:
                print(cls, file=file)


        with open ('pars.txt', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace(", ", "', '")   
        with open ('pars.txt', 'w') as f:
            f.write(new_data)
        with open ('pars.txt', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("  —  ", "', '")   
        with open ('pars.txt', 'w') as f:
            f.write(new_data)
        with open ('pars.txt', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<br/><b>", "', '") 
        with open ('pars.txt', 'w') as f:
            f.write(new_data)
        with open ('pars.txt', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("</b><br/>", "', '")  
        with open ('pars.txt', 'w') as f:
            f.write(new_data)
        with open ('pars.txt', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("<p>", "('") 
        with open ('pars.txt', 'w') as f:
            f.write(new_data)
        with open ('pars.txt', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("</p>", "')")   
        with open ('pars.txt', 'w') as f:
            f.write(new_data)
        with open ('pars.txt', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("'Классный час</b>'", "'Классный час', 'Классный час', 'Классный час'")  
        with open ('pars.txt', 'w') as f:
            f.write(new_data)
        with open ('pars.txt', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace("""<a href="/">На сайт</a>""", "00:00', '00:00', '00:00', '00:00', '00:00") 
        with open ('pars.txt', 'w') as f:
            f.write(new_data)