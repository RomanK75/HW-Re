from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re
#PHONE
# (\+7|8|7)\s*?\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{2})[- ]?(\d{2})( [(]?)?([Д-д]об. \d{4})? reg101 phone
# +7(\g<2>)\g<3>-\g<4>-\g<5>\ \g<7>
# FIO
#([А-ЯЁ]{1}[а-яё]+)[ ,]([А-ЯЁ]{1}[а-яё]+)[ ,]([А-ЯЁ]{1}[а-яё]+)?,"
# \g<1>,\g<2>,\g<3>,
# final r"(^[а-яёА-ЯЁ]*),([а-яёА-ЯЁ]+),([а-яёА-ЯЁ]+)?,,?,?,?,?([а-яёА-ЯЁ]+)?,([^,]*)?,(\+7\(\d*\)\d*-..-.. ?доб.(\d{4})?)?,(.*)"
# Function
def main():
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        print('------BEGINING-----')
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        text_contact = ''
        for string in contacts_list:
            text_contact += ','.join(string) + "\n"
        print('------RAW TXT-----')
        print(text_contact)
        pattern= r"(\+7|8|7)\s*?\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{2})[- ]?(\d{2}) ?(\(?((доб. )(\d{4}))\)?)?"
        new_pattern = r"+7(\g<2>)\g<3>-\g<4>-\g<5> доб.\g<9>"
        text_contact = re.sub(pattern, new_pattern, text_contact)
        print('------PHONE CORRECTION-----')
        print(text_contact)
        pattern= r"([А-ЯЁ]{1}[а-яё]+)[ ,]([А-ЯЁ]{1}[а-яё]+)[ ,]([А-ЯЁ]{1}[а-яё]+)?,"
        new_pattern = r"\g<1>,\g<2>,\g<3>,"
        text_contact = re.sub(pattern, new_pattern, text_contact)
        print('------NAME CORRECTION-----')
        print(text_contact)
        pattern = r"([а-яёА-ЯЁ]*),([а-яёА-ЯЁ]+),([а-яёА-ЯЁ]+)?,,?,?,?,?([а-яёА-ЯЁ]+)?,([^,]*)?,(\+7\(\d*\)\d*-..-.. ?доб.(\d{4})?)?,(.*)"
        new_pattern = r'\g<1>,\g<2>,\g<3>,\g<4>,\g<5>,\g<6>\g<7>,\g<8>'
        text_contact = re.sub(pattern,new_pattern, text_contact)
        print('------SECTION CORRECTION-----')
        print(text_contact)
        contact_list = text_contact.split('\n')
        new_cl = []
        for ppl in contact_list:
            new_cl.append(ppl.split(','))
        del new_cl[-1]
        pprint(new_cl)
        print('------END-----')
        clone_list = new_cl[:]
        # Туда надо разобраться с дублями.......

            

            
        
 
            


    ## 2. Сохраните получившиеся данные в другой файл.
    ## Код для записи файла в формате CSV:
    #with open("phonebook.csv", "w") as f:
        # datawriter = csv.writer(f, delimiter=',')
    
    ## Вместо contacts_list подставьте свой список:
    #datawriter.writerows(contacts_list)

## Exe function

if __name__ == '__main__':
    main()