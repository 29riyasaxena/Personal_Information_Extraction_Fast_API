from fastapi import FastAPI
import spacy
from pydantic import BaseModel
import spacy
import en_core_web_sm
import regex as re

string = input()

def get_person_name(string):
    nlp = en_core_web_sm.load()
    doc = nlp(string)
    for token in doc.ents:
        if token.label_=="PERSON":
            print(token.label_, token.text)
    
app = FastAPI(tags=['sentence'])

def get_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    #print("Email Adress")
    return [print("Email Address")],[print(r.findall(string))]

def get_url(string):
    regex = r"((https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}))"
    url = re.findall(regex,string)
    return [print("URL")],[print(url)]

def get_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    x = (re.sub(r'\D', '', num) for num in phone_numbers)
    return [print("Phone number")],[print(phone_numbers)]

class Input(BaseModel):
   sentence: str
@app.post("/analyze_text")
def get_text_characteristics(sentence_input: Input):
    document = nlp(sentence_input.sentence)
    output_array = []
    for token in document:
        output = {
            "Index": token.i, "Token": token.text, "Tag": token.tag_, "POS": token.pos_,
            "Dependency": token.dep_, "Lemma": token.lemma_, "Shape": token.shape_,
            "Alpha": token.is_alpha, "Is Stop Word": token.is_stop
        }
        output_array.append(output)
    return {"output": output_array}
get_person_name(string)
get_email_addresses(string)
get_phone_numbers(string)
get_url(string)