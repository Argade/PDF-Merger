#importing necessary modules
from PyPDF4 import PdfFileReader, PdfFileMerger
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def merge_pdf():
    facility = request.form.get('Facility')

    #reading data file
    data = pd.read_excel("BMR-BPR FORMAT ISSUANCE INDEX.xlsx")

    #grouping Facility data into variable
    data1 = data[data['FACILITY'] == facility]

    #Storing Annexures and Quantity Required PDF.
    pdf_files = data1['Format  (Annexure) No. '].tolist()
    quantities = data1['Quantity'].tolist()

    #Calling PDFMerger object and storing it in variable named.
    merger = PdfFileMerger()

    #Performing operations on Requireed group's PDF's.
    for pdf, quantity in zip(pdf_files, quantities):
        reader = PdfFileReader(pdf, 'rb'):
            for _ in range(quantity):
                merger.append(reader)

    #Creating file of Merged PDF's
    with open("merged_pdf.pdf", 'wb') as file:
        merger.write(file)
    return "PDF merging completed successfully."

if __name__ == '__main__':
    app.run()
