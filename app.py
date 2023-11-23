import streamlit as st
from PIL import Image

def main():
    st.title("Image Viewer")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        before_image = Image.open(uploaded_file)
        st.image(before_image, caption="Before Image", use_column_width=True)

        if st.button("Display After Image"):
            # Load or process your "after" image here
            # For demonstration, let's use the same image as "after" for simplicity
            after_image = before_image
            st.image(after_image, caption="After Image", use_column_width=True)

        if st.button("Display Difference Image"):
            # Load or process your "difference" image here
            # For demonstration, let's use a blank image as "difference" for simplicity
            difference_image = Image.new("RGB", before_image.size)
            st.image(difference_image, caption="Difference Image", use_column_width=True)

if  __name__ == "__main__":
    main()
