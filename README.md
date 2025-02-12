# OrganizeMe

**OrganizeMe** is a desktop application designed to help users organize their tasks, notes, and files in one place. With a focus on simplicity and customization, OrganizeMe is perfect for students, professionals, and anyone who needs a centralized tool for managing their daily tasks and notes.

---

## Features

### Core Features

1. **Note-Taking Section**:
   - Create and manage notebooks, sections, and pages.
   - Supports both plain text pages and Excel-like sheets.
   - Rich text formatting (bold, italic, underline, etc.).
   - Automatic saving via JSON files.

2. **Calendar**:
   - Manage events and tasks in a calendar view.
   - Save and load events using JSON files.

3. **File and Document Storage**:
   - Store and organize files locally.
   - Easy access to files directly from the application.

4. **Customizable Dashboard**:
   - Drag-and-drop widgets to rearrange sections.
   - Adjustable window size and layout.

5. **Settings**:
   - Customize the appearance of the application (colors, layout, etc.).
   - Save settings persistently using JSON files.

---

## Technical Stack

- **Front-end**: PyQt6 for the user interface.
- **Back-end**: Python for application logic.
- **Data Storage**: JSON files for notebooks, calendar events, and settings.
- **Fonts**: Custom font family (Comme) for a consistent look and feel.

---

## Installation

### Prerequisites

- Python 3.9 or higher.
- Git (optional, for cloning the repository).

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/OrganizeMe.git
   cd OrganizeMe
   pip install -r requirements.txt
   python main.py