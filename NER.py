import streamlit as st
import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
def extract (text):
    doc=nlp(text)
    entites=[(ent.text,ent.label_)for ent in doc.ents]
    return entites
def show_ner(doc):
    html = displacy.render(doc,style="ent",jupyter=False)
    return html
st.title("Text Extraction using spacy")
st.write("please enter text . . .")
text=st.text_area("Please enter text to extract entities",height=200)
if st.button("Extract") :
    if text :
        doc = nlp(text)
        entities = extract(doc)
        st.write(entities)
        st.subheader("Extract entites")
        st.markdown(show_ner(doc),unsafe_allow_html=True)
