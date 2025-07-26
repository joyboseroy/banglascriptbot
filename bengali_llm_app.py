# Bengali Learning LLM App (BanglaScriptBot)
# Updated to use indic-transliteration for Banglish to Bengali script conversion

import streamlit as st
from indic_transliteration.sanscript import transliterate
from indic_transliteration.sanscript import ITRANS, BENGALI

st.set_page_config(page_title="BanglaScriptBot", page_icon=None)
st.title("BanglaScriptBot: Learn Bengali Script from Banglish")

st.markdown("""
This app helps you convert spoken-style or phonetic Bengali (Banglish) into formal Bengali script
using a lightweight transliteration engine (`indic-transliteration`).
Type something like `ami tomar sathe jete chai` and get a grammar-correct Bengali sentence.
""")

# User Input
user_input = st.text_area("Enter your Banglish (phonetic Bengali or spoken-style):", height=100)

# Conversion function using indic-transliteration
def convert_banglish_to_bengali(text):
    return transliterate(text, ITRANS, BENGALI)

if st.button("Convert to Bengali") and user_input:
    with st.spinner("Converting using transliteration..."):
        output = convert_banglish_to_bengali(user_input)
    st.success("Formal Bengali:")
    st.write(output.strip())

st.markdown("---")
st.markdown("Made with love using indic-transliteration and Streamlit | [GitHub Repo](#)")
