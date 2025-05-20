import os
import shutil
from pathlib import Path
from collections import defaultdict
from abc import ABC, abstractmethod

# ---------------------- Base Organizer (Parent Class) ----------------------
class BaseOrganizer(ABC):
    """Abstract base class for all file organizers."""
    
    def __init__(self, directory: str):
        self.directory = Path(directory)
        self.summary = defaultdict(int)

    @abstractmethod
    def organize(self, dry_run: bool = False, delete_empty: bool = False) -> dict:
        """Main method to organize files. Must be implemented by child classes."""
        pass

    def _delete_empty_folders(self, original_files: list) -> None:
        """Deletes empty folders after organization."""
        for item in self.directory.iterdir():
            if item.is_dir() and item.name not in self.summary:
                try:
                    if not any(item.iterdir()):  # Folder is empty
                        item.rmdir()
                except (PermissionError, OSError) as e:
                    print(f"⚠️ Could not delete {item}: {e}")

# ---------------------- FileTypeManager (Same as Before) ----------------------
class FileTypeManager:
    def __init__(self):
        self.file_map = {
            "Images": [".jpg", ".jpeg", ".png", ".gif"],
            "Documents": [".pdf", ".docx", ".txt", ".doc", ".xlsx"],
            "Media": [".mp4", ".mp3", ".wav"],
            "Archives": [".zip", ".rar", ".7z"],
            "Software": [".exe", ".msi", ".apk"],
            "Others": []
        }

    def get_category(self, extension):
        for category, extensions in self.file_map.items():
            if extension.lower() in extensions:
                return category
        return "Others"

# ---------------------- FileOrganizer (Default Organizer) ----------------------
class FileOrganizer(BaseOrganizer):
    """Default organizer for all file types."""
    
    def __init__(self, directory: str):
        super().__init__(directory)
        self.type_manager = FileTypeManager()

    def organize(self, dry_run: bool = False, delete_empty: bool = False) -> dict:
        if not self.directory.exists():
            raise ValueError("Directory does not exist!")

        original_files = list(self.directory.iterdir())

        for file in original_files:
            if file.is_file():
                ext = file.suffix
                category = self.type_manager.get_category(ext)
                target_folder = self.directory / category
                
                if not dry_run:
                    target_folder.mkdir(exist_ok=True)
                    shutil.move(str(file), str(target_folder / file.name))
                
                self.summary[category] += 1

        if delete_empty:
            self._delete_empty_folders(original_files)

        return dict(self.summary)

# ---------------------- DocumentOrganizer (Specialized for Docs) ----------------------
class DocumentOrganizer(BaseOrganizer):
    """Organizes only documents (PDF, DOCX, TXT, etc.)."""
    
    def __init__(self, directory: str):
        super().__init__(directory)
        self.doc_extensions = [".pdf", ".docx", ".txt", ".doc", ".xlsx"]

    def organize(self, dry_run: bool = False, delete_empty: bool = False) -> dict:
        if not self.directory.exists():
            raise ValueError("Directory does not exist!")

        original_files = list(self.directory.iterdir())

        for file in original_files:
            if file.is_file() and file.suffix.lower() in self.doc_extensions:
                target_folder = self.directory / "Documents"
                
                if not dry_run:
                    target_folder.mkdir(exist_ok=True)
                    shutil.move(str(file), str(target_folder / file.name))
                
                self.summary["Documents"] += 1

        if delete_empty:
            self._delete_empty_folders(original_files)

        return dict(self.summary)

# ---------------------- VideoOrganizer (Specialized for Videos) ----------------------
class VideoOrganizer(BaseOrganizer):
    """Organizes only video files (MP4, MKV, AVI, etc.)."""
    
    def __init__(self, directory: str):
        super().__init__(directory)
        self.video_extensions = [".mp4", ".mkv", ".avi", ".mov"]

    def organize(self, dry_run: bool = False, delete_empty: bool = False) -> dict:
        if not self.directory.exists():
            raise ValueError("Directory does not exist!")

        original_files = list(self.directory.iterdir())

        for file in original_files:
            if file.is_file() and file.suffix.lower() in self.video_extensions:
                target_folder = self.directory / "Videos"
                
                if not dry_run:
                    target_folder.mkdir(exist_ok=True)
                    shutil.move(str(file), str(target_folder / file.name))
                
                self.summary["Videos"] += 1

        if delete_empty:
            self._delete_empty_folders(original_files)

        return dict(self.summary)