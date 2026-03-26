import streamlit as st
from output_structure import analyze_drawing

st.title("Seam breakdown and BOM")
uploaded_file = st.file_uploader("Upload a tech pack drawing", type=["jpg","pdf", "jpeg", "png", "webp"])

if uploaded_file:
    #save temporarily
    with open("temp_upload.png", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    with st.spinner("Analyzing drawing..."):
        result = analyze_drawing("temp_upload.png")

    st.subheader("Stitch Breakdown")
    st.dataframe([row.model_dump() for row in result.stitch_table])

    st.subheader("Bill of Materials")
    st.dataframe([row.model_dump() for row in result.bom])

    st.subheader("Fabrics")
    st.dataframe([row.model_dump() for row in result.fabrics])