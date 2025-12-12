!pip install streamlit
import streamlit as st
import numpy as np
import joblib
from wordcloud import WordCloud
import matplotlib.pyplot as plt
st.title("PDF Keyword Extractor")
st.write("Upload a PDF & enter keywords to extract paragraphs.")
# PDF Upload Box
uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])
# Keyword extractor
if st.button("Extract"):
    if uploaded_pdf is None:
        st.warning("Please upload a PDF.")
    else:
        # Extract full text from PDF
        text = extract_text_from_pdf(uploaded_pdf)

        if text.strip() == "":
            st.warning("The PDF has no readable text.")
        else:
                      # Convert keywords to lowercase list
            keywords = [k.strip().lower() for k in keywords_input.split(",")]

            # Split text into paragraphs
            paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

            # Extract paragraphs containing ANY keyword
            extracted = []
            for para in paragraphs:
                p_low = para.lower()
                if any(k in p_low for k in keywords):
                    extracted.append(para)

            # Display extracted paragraphs
            st.subheader("Extracted Paragraphs Containing Keywords")
            if len(extracted) == 0:
                st.info("No matching paragraphs found.")
            else:
                for i, p in enumerate(extracted, 1):
                    st.write(f"**Paragraph {i}:**")
                    st.write(p)
                    st.write("---")

                # ---- Word Cloud ----
                st.subheader("Word Cloud (From Extracted Text)")
                all_text = " ".join(extracted)

                wc = WordCloud(width=900, height=400).generate(all_text)

                plt.figure(figsize=(10, 4))
                plt.imshow(wc, interpolation="bilinear")
                plt.axis("off")
                st.pyplot(plt)
