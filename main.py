# Código do dev aqui
def standardize_names(character_name):
    character_name = character_name.strip()
    character_name = character_name.replace(" ", "-")
    return character_name

    
def standardize_title(text):
    return text.title()

def standardize_text(text):
    text = list(text)
    for index,letter in enumerate(text):
        if index == 0 : 
            text[0] = text[0].upper()
        if letter == '.' and index != len(text) - 1:
            text[index+2] = text[index+2].capitalize()
    return "".join(text)
standardize_text("a  famosa atriz    Constance  ")
def title_creator(text):
    text = text.title()
    hifen = ['-' for i in range(20)]
    hifen = "".join(hifen)
    return hifen+text+hifen


def text_merge(text_a, text_b=''):
    text_a = text_a.split()
    text_a[0] = text_a[0].capitalize()
    text_a = " ".join(text_a)
    if(text_a[len(text_a)-1] == '.'):
        text_a = text_a[:-1:]
    text_b = text_b.split()
    text_b[0] = text_b[0].lower()
    text_b= " ".join(text_b)
    print( text_a+ text_b)
    return standardize_text(text_a+" "+text_b)

