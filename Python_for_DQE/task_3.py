import re

text_variable = "homEwork:\n\n tHis iz your homeWork, copy these Text to variable.\n\n You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.\n\n it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.\n\n last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."

def new_sentences(text):
    text = re.sub(r"\biz\b",'is',text)
    sentences = text.split('.')
    last_words = [sentence.split()[-1] for sentence in sentences if sentence]
    new_text= text + ' ' + ' '.join(last_words)
    count_of_whitespaces = 0
    for i in new_text:
        if i.isspace():
            count_of_whitespaces += 1
    return new_text.capitalize(), count_of_whitespaces


print(new_sentences(text_variable))






