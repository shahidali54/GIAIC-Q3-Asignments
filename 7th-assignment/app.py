import streamlit as st
import os
from file_organizer import FileOrganizer, DocumentOrganizer, VideoOrganizer  # Updated import
from tempfile import TemporaryDirectory

# Set dark/light theme toggle
st.set_page_config(page_title="🗂️ Smart File Organizer", layout="centered")

st.title("🗂️ Smart File Organizer")
st.markdown("Organize your folder automatically by file types with cool features ")

DARK_MODE_CSS = """
<style>
    /* Main page background */
    .stApp {
        background-color: #0E1117;
    }
    
    /* All text color */
    .css-1v0mbdj, .css-1q8dd3e, .css-1cpxqw2, h1, h2, h3, h4, h5, h6, p, div, span {
        color: #FAFAFA !important;
    }
    
    /* Input fields */
    .stTextInput input, .stSelectbox select, .stTextArea textarea {
        background-color: #262730 !important;
        color: white !important;
        border-color: #444 !important;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #4F8BF9;
        color: white;
        border: none;
    }
    
    /* Checkboxes */
    .stCheckbox label {
        color: white !important;
    }
    
    /* File uploader */
    .stFileUploader label {
        color: white !important;
    }
    
    /* JSON viewer */
    .stJson {
        background-color: #1E1E1E !important;
    }
    
    /* Divider line */
    hr {
        border-color: #444 !important;
    }
</style>
"""

# Theme toggle
with st.sidebar:
    dark_mode = st.toggle("🌗 Dark Mode", value=False)


if dark_mode:
    st.markdown(DARK_MODE_CSS, unsafe_allow_html=True)

# File Uploader (for single files - optional)
st.subheader("📤 Drag & Drop Single File")
uploaded_file = st.file_uploader("Upload a file to test (not required)", type=None)

if uploaded_file:
    with TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, uploaded_file.name)
        with open(filepath, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"Uploaded to temp path: {filepath}")
        if st.button("Organize This File"):
            organizer = FileOrganizer(tmpdir)  # Default organizer for single file
            summary = organizer.organize()
            st.write("### ✅ Summary:")
            st.json(summary)

st.divider()

# Main Folder Organizer
st.subheader("📁 Full Folder Path")
folder_path = st.text_input("Enter folder path here")

# 🔥 NEW: Organizer Type Dropdown
organizer_type = st.selectbox(
    "Select Organizer Type",
    ("Default (All Files)", "Only Documents", "Only Videos"),
    help="Choose which type of files to organize"
)

col1, col2 = st.columns(2)
with col1:
    dry_run = st.checkbox("🔍 Preview only (Dry Run)")
with col2:
    delete_empty = st.checkbox("🗑️ Delete empty folders")

if st.button("Organize Now"):
    if folder_path:
        try:
            # 🔥 NEW: Select organizer based on dropdown choice
            if organizer_type == "Default (All Files)":
                organizer = FileOrganizer(folder_path)
            elif organizer_type == "Only Documents":
                organizer = DocumentOrganizer(folder_path)
            elif organizer_type == "Only Videos":
                organizer = VideoOrganizer(folder_path)

            summary = organizer.organize(dry_run=dry_run, delete_empty=delete_empty)

            if dry_run:
                st.info("Dry run completed. The following changes **would** happen:")
            else:
                st.success("Files organized successfully! ✅")

            st.write("### 📊 File Summary:")
            st.json(summary)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid path")
        