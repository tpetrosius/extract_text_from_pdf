import os, PyPDF2, openpyxl, sys, datetime
from extract_text_from_pdf import extract_values
from get_EURSEK_rate import get_EURSEK_rate
from create_final_report import create_final_report
from write_data_to_final_report import write_data

#Get absolute file paths in directory.	
file_paths = []

for folder, subs, files in os.walk(r"C:\Users\Vartotojas\Desktop\Reports"):
	for filename in files:
		file_paths.append(os.path.abspath(os.path.join(folder, filename)))
		
number_of_file_paths = len(file_paths)

if number_of_file_paths == 0:
	print("No report to process.")
	sys.exit()

#Get SEK rate from investing.com.
SEK_rate = get_EURSEK_rate()

#Create Final Report where data will be stored.
final_report = create_final_report()
print('Final Report to store extracted data was created...\n\n')

# Loop each report in list and do the process.
number_of_report = 1
for file_path in file_paths:		
	if ".pdf" not in file_path:
		continue
	else:
		
		pdf_obj = open(file_path, 'rb')
		pdfReader = PyPDF2.PdfFileReader(pdf_obj)
		pdf_page = pdfReader.getPage(0)
		pdf_ver_1 = pdf_page.extractText()
		pdf_ver_2 = pdf_ver_1.replace("\n", "")
		pdf_text = pdf_ver_2.replace("_", "")
		
		# Extract values to dictionary.
		values = extract_values(pdf_text)
		print('Data was extracted from report no. ' + str(number_of_report) + '...\n\n')
		
		save_data = write_data(final_report, values, SEK_rate)
		
		number_of_report += 1

#Exit process
print("Process has been completed...")
sys.exit()
