#https://python-docx.readthedocs.io/en/latest/
from docx import Document
from docx.shared import Inches
import os
import sys


def open_docx(file):
	doc = Document(file)
	return doc


def process_document (report_list, files_list, output_folder):

	for i in range(len(report_list)):
		doc = open_docx (report_list[i])
		doc.paragraphs[0].text = 'XXXXXX'
		cont = 0
		for p in doc.paragraphs:
			#print p.text
			if 'Paciente:' in p.text:
				break
			cont=cont+1
		doc.paragraphs[cont].text = 'Paciente: XXXXXXXXXX'
		output = output_folder + "decharacterized_" + files_list[i]

		doc.save(output)


def get_reports_filename_in_folder(folder):
	report_list = []
	files_list = []
	for root, dirs, files in os.walk(folder):
		for file in files:
			if file.endswith('.docx'):
				report_list.append(file)
				files_list.append(file)

	for i in range(len(report_list)):
		report_list[i] = folder + report_list[i]

	return report_list, files_list


def main():
	#print len(sys.argv)
	if len(sys.argv) < 3:
		print("Incorrect input!")
		print("The right way: python report_editor.py <reports_folder> <output_folder>")
		exit(1)

	report_list = []
	files_list = []
	report_list, files_list = get_reports_filename_in_folder(sys.argv[1])
	#doc = open_docx()
	process_document (report_list, files_list, sys.argv[2])
  
if __name__== "__main__":
	main()

#document.add_heading('Document Title', 0)

#p = document.add_paragraph('A plain paragraph having some ')
#p.add_run('bold').bold = True
#p.add_run(' and some ')
#p.add_run('italic.').italic = True

#document.add_heading('Heading, level 1', level=1)
#document.add_paragraph('Intense quote', style='Intense Quote')

#document.add_paragraph(
#    'first item in unordered list', style='List Bullet'
#)
#document.add_paragraph(
#    'first item in ordered list', style='List Number'
#)

#document.add_picture('monty-truth.png', width=Inches(1.25))

#records = (
#    (3, '101', 'Spam'),
#    (7, '422', 'Eggs'),
#    (4, '631', 'Spam, spam, eggs, and spam')
#)

#table = document.add_table(rows=1, cols=3)
#hdr_cells = table.rows[0].cells
#hdr_cells[0].text = 'Qty'
#hdr_cells[1].text = 'Id'
#hdr_cells[2].text = 'Desc'
#for qty, id, desc in records:
#    row_cells = table.add_row().cells
#    row_cells[0].text = str(qty)
#    row_cells[1].text = id
#    row_cells[2].text = desc

#document.add_page_break()

#document.save('demo.docx')
