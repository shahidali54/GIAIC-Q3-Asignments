
# 🗂️ Smart File Organizer

This is a simple and smart file organizer built using **Python** and **Streamlit**. It allows you to organize your files in a folder based on type (e.g., documents, videos, images, etc.). It also includes options like previewing (dry run), deleting empty folders, and organizing only specific file types.

## 🌟 Features

- Organize files by type: Images, Videos, Documents, etc.
- Choose specific organizer: Default / Documents only / Videos only.
- Dark Mode toggle for better UX.
- Option to delete empty folders.
- Drag & Drop single file to test the organization.
- Dry run support to preview changes without modifying files.

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python (OOP-based file organizers)

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/your-username/smart-file-organizer.git
cd smart-file-organizer
```

### Install dependencies

```bash
pip install streamlit
```

### Run the app

```bash
streamlit run frontend.py
```

## 📁 Folder Structure

```
smart-file-organizer/
├── frontend.py
├── file_organizer.py
├── README.md
```

## 📦 Organizer Types

- **Default (All Files):** Organizes everything by type.
- **Only Documents:** Organizes only .pdf, .docx, .txt, .xlsx.
- **Only Videos:** Organizes only .mp4, .mkv, .avi, .mov.

## 🌓 Dark Mode Support

Toggle dark mode from the sidebar for a better visual experience.

## 🧪 Dry Run Mode

Check what changes would be made without actually moving any files.

## 🧹 Delete Empty Folders

Enable this option to clean up empty folders after organizing.

## 📬 Feedback / Issues

Feel free to open issues or pull requests if you find bugs or have feature suggestions.

---

Made with ❤️ using Python and Streamlit.
