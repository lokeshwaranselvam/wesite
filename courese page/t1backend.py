from flask import Flask, request, render_template_string
import openpyxl
import os

app = Flask(__name__)

# Path to your HTML file
HTML_PATH = r"C:\Users\lokeshwaran\OneDrive\Desktop\Shanky hawks international private limited\courese page\t1\data_science.html"

# Path to your Excel file
EXCEL_PATH = r"C:\Users\lokeshwaran\OneDrive\Desktop\Shanky hawks international private limited\data applied\data science.xlsx"

@app.route('/')
def form():
    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        html_content = f.read()
    return render_template_string(html_content)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form

    # Create workbook if file doesn't exist
    if not os.path.exists(EXCEL_PATH):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Applications"
        ws.append(["Name", "Email", "Phone", "Education", "Profession", "Graduation", "WhatsApp", "City"])
    else:
        wb = openpyxl.load_workbook(EXCEL_PATH)
        ws = wb.active

    # Append data to Excel
    ws.append([
        data.get("name"),
        data.get("email"),
        data.get("phone"),
        data.get("education"),
        data.get("profession"),
        data.get("graduation"),
        data.get("whatsapp"),
        data.get("city"),
    ])

    wb.save(EXCEL_PATH)
    return "✅ Application submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
