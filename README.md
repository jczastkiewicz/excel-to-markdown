# EXCEL-TO-MARKDOWN

![License](https://img.shields.io/badge/license-GPLv3-blue)
![Python](https://img.shields.io/badge/python-3.1%2B-blue.svg)

**EXCEL-TO-MARKDOWN** is a robust Python tool designed to convert Excel files (`.xlsx` and `.xls`) into well-formatted Markdown tables. Leveraging a modular architecture, this tool offers enhanced table detection capabilities, interactive prompts for handling complex Excel layouts, and seamless integration with various project workflows.

## 🛠️ Features

- **Automated Table Detection:** Identifies the first fully populated row as the table header, ensuring accurate Markdown conversion.
- **Interactive Mode:** Prompts users to specify table regions when automatic detection fails, handling complex and irregular Excel structures.
- **Modular Design:** Organized into distinct modules for detection, parsing, Markdown generation, and utilities, promoting maintainability and scalability.
- **Supports Multiple Sheets:** Processes all sheets within an Excel file, generating separate Markdown files for each.
- **Flexible Column Specification:** Allows users to define column ranges using both letter-based (e.g., `A:D`) and number-based (e.g., `1-4`) inputs.
- **Unit Tested:** Comprehensive unit tests ensure reliability and facilitate future enhancements.
- **Easy Integration:** Compatible with Poetry for dependency management and can be integrated into larger projects or CI/CD pipelines.

## 📁 Project Structure

```
EXCEL-TO-MARKDOWN
│
├── .venv
├── data
│   ├── input
│   └── output
├── docs
├── excel_to_markdown
│   ├── __init__.py
│   ├── main.py
│   ├── detector.py
│   ├── parser.py
│   ├── markdown_generator.py
│   └── utils.py
├── src
├── tests
│   ├── test_detector.py
│   ├── test_parser.py
│   ├── test_markdown_generator.py
│   └── test_main.py
├── .gitignore
├── LICENSE
├── poetry.lock
├── pyproject.toml
└── readme.md
```

### **Module Breakdown**

- **`excel_to_markdown/`**
  - **`main.py`**: Entry point of the application. Handles argument parsing, orchestrates the workflow, and manages file I/O.
  - **`detector.py`**: Contains functions related to detecting the table start within Excel sheets.
  - **`parser.py`**: Handles parsing user inputs, such as column specifications.
  - **`markdown_generator.py`**: Responsible for converting pandas DataFrames to Markdown format.
  - **`utils.py`**: Utility functions like column letter to index conversion and filename sanitization.

- **`tests/`**
  - **`test_detector.py`**
  - **`test_parser.py`**
  - **`test_markdown_generator.py`**
  - **`test_main.py`**
  
  *Each test file contains unit tests for their respective modules, ensuring functionality and reliability.*

## 🚀 Installation

You can install `excel-to-markdown` directly from this repository using `pip`:

```bash
pip install git+https://github.com/devin-liu/excel-to-markdown.git
```
*Note: This assumes the repository URL is `github.com/devin-liu/excel-to-markdown`.*


### For Development

If you want to contribute to the project, it is recommended to use [Poetry](https://python-poetry.org/) for managing dependencies and the development environment.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/devin-liu/excel-to-markdown.git
    cd excel-to-markdown
    ```

2.  **Install dependencies with Poetry:**
    ```bash
    poetry install
    ```
This will create a virtual environment and install all the necessary dependencies.

## 📋 Usage

### **Preparing Your Data**

1. **Input Directory:** Place all your Excel files (`.xlsx` or `.xls`) in the `data/input` directory.

2. **Output Directory:** The converted Markdown files will be saved in the `data/output` directory by default. If this directory doesn't exist, the script will create it.

- **`data/input`**: Directory containing your Excel files.
- **`data/output`**: (Optional) Directory where Markdown files will be saved. If not specified, an `output` folder will be created inside the input directory.


### **Running the Localhost Server**

You can also start a localhost server for real-time editing using the `app` command:

```bash
app
```

This will start a server on your localhost, allowing you to make edits to your spreadsheets locally and see immediate updates.

### **Running the CLI Script** 

Execute the main script over CLI using the `excel-to-markdown` command:

```bash
excel-to-markdown data/input data/output
```

### **Interactive Prompts**

For each sheet in each Excel file:

1. **Automatic Detection:**
   - The script attempts to detect the header row based on the enhanced logic (first fully populated row).
   - If successful, it proceeds to convert without prompts.

2. **Manual Specification:**
   - If automatic detection fails, you'll be prompted to enter:
     - **Header Row Number:** The row where your table headers are located (1-based index).
     - **Columns to Include:** Specify the range of columns, e.g., `A:D` or `1-4`.

**Sample Interaction:**

```
Processing sheet: 'Sales Data' in file 'report1.xlsx'
Automatically detected table starting at row 2.
Markdown file 'report1_Sales_Data.md' for sheet 'Sales Data' has been created successfully.

Processing sheet: 'Summary' in file 'report1.xlsx'
Automatic table detection failed.
Enter the header row number (1-based index): 5
Enter the columns to include (e.g., A:D or 1-4): B:E
Markdown file 'report1_Summary.md' for sheet 'Summary' has been created successfully.
```

## 🧩 Contributing

Contributions are welcome! To contribute:

1. **Fork the Repository**

2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add some feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeatureName
   ```

5. **Open a Pull Request**

Please ensure that your contributions adhere to the existing code style and include relevant tests.

## 🧪 Testing

Unit tests are located in the `tests/` directory. To run the tests, first install the development dependencies:

```bash
pip install -e .[dev]
```
Then run pytest:
```bash
pytest
```

For contributors using Poetry, you can still run the tests with:
```bash
poetry run pytest
```

## 📜 License

This project is licensed under the [GPLv3](LICENSE).

## 📧 Contact

For any inquiries or support, please contact [devin.r.liu@gmail.com](mailto:devin.r.liu@gmail.com).

---

**Happy Converting! 🚀**

---