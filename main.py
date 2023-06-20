from pprint import pprint
import csv
import re

def parser(text):
    pattern_dict = {
    'fio': {
    'regexp': r'(\w+)( |,)(\w+)( |,)(\w+|),(,+|)(,,,|[А-Яа-я]+)',
    'subst': r"\1,\3,\5,\7"
    },
    'phone': {
    'regexp': r'(\+\d|\d)\s*(\(|)(\d{3})[\s\)-]*(\d{3})\-*(\d{2})\-*(\d{2})',
    'subst': r'+7(\3)\4-\5-\6'
    },
    'add_phone': {
    'regexp': r'\(?доб\.\s(\d+)\)*',
    'subst': r'доп.\1'
    }
    }
    for command in pattern_dict.values():
        for exp in command.items():
            if exp[0] == 'regexp':
                regexp = exp[1]

            else:
                subst = exp[1]

        text = re.sub(regexp, subst, text)

    return text
def double_killing(ls):
    result = {}
    for string in ls:
        if string[0]+' '+ string[1] not in result:
            result[string[0]+' '+ string[1]] = string[2:]
        else:
            new_info = string[2:]
            old_info = result.get(string[0]+' '+ string[1])
            for i in range(len(new_info)):
                if new_info[i] == '':
                    new_info[i] = old_info[i]
            result[string[0]+' '+ string[1]] = new_info
    new_list = []
    for key,value in result.items():
        string = key.split()
        for info in value:
            string.append(info)
        new_list.append(string)
    return new_list
    

def main():
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        # Reading csv file
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        text_contact = ''
        for string in contacts_list:
            text_contact += ','.join(string) + "\n"
        # Using Re
        new_text = parser(text_contact)
        # Convert to list
        contact_list = new_text.split('\n')
        new_cl = []
        for ppl in contact_list:
            new_cl.append(ppl.split(','))
        del new_cl[-1]
        for i in range(len(new_cl)):
            if len(new_cl[i]) > 7:
                new_cl[i] = new_cl[i][:7]
        # Data merge
        resolved = double_killing(new_cl)
        # Writing to new file
    with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(resolved)
    # end

## Exe function

if __name__ == '__main__':
    main()