#Imports
import json

import datetime

from common import *
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, PageBreak, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle

#global variables
top_logo_path = 'images/top_logo.jpg'
doc = SimpleDocTemplate("pdfs/list.pdf", pagesize=A4)
doc.topMargin = 1 * cm
doc.bottomMargin = 1 * cm

image = Image(top_logo_path, 20 * cm, 5 * cm)

flowables = []    

date_style = ParagraphStyle('date_style', alignment=1, fontSize=10, leading=10*1.5, fontName='Times-Roman')
today = datetime.date.today();
gen_date = Paragraph(str(today), date_style)

def pdf_generation_all():
    pdf_generation_list()
    pdf_generation_confirmation()

    doc.build(flowables)
    print("[INFO]: PDF generated")
    check_clear();     

def pdf_generation_confirmation():
    with open(DEF_DB_NAME, mode="r", encoding="utf-8") as db_f:
        db = json.load(db_f);
    
    flowables.append(gen_date);
    table1 = [["Catégories", "Versement", "Confirmation"]]
    
    for categories in db:
        if categories != "Commandes":
            table1.append([categories, "", ""])
            flowable_table1 = Table(table1, colWidths=[13 * cm, 4 * cm, 3 * cm])
            flowable_table1.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 1, colors.black),
                                            ('FONT', (0,0), (-1,0), 'Times-Bold', 10, 12),
                                            ('FONT', (0,1), (-1,-1), 'Times-Roman', 10,12)]))
    
    flowables.append(flowable_table1)
    page_title_style = ParagraphStyle('main_style', alignment=1, fontSize=20, leading=20*1.5, fontName="Times-Bold")
    page_title = Paragraph("Autre", page_title_style)
    flowables.append(page_title)
    table2 = [["Nom", "Prix"]]
    for i in range(10):
        table2.append(["",""])
    flowable_table2 = Table(table2, colWidths=[17 * cm, 3 * cm])
    flowable_table2.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 1, colors.black),
                                        ('FONT', (0,0), (-1,-1), 'Times-Roman', 10,12)]))
     
    flowables.append(flowable_table2)

    





def pdf_generation_list():

    with open(DEF_DB_NAME, mode="r", encoding="utf-8") as db_f:
        db = json.load(db_f);

    flowables.append(gen_date);

    for categories in db:
        flowables.append(image)
        page_title_style = ParagraphStyle('main_style', alignment=1, fontSize=20, leading=20*1.5, fontName="Times-Bold")
        page_title = Paragraph(categories, page_title_style)
        flowables.append(page_title)

        #creating the tables
        table = [['Nom', 'Marque', 'Référance', "Quantité"]]
        for elem in db[categories]:
            item = [elem['name'], elem['brand'], elem['ref'], elem['qnt']]
            table.append(item)
        
        flowable_table = Table(table, colWidths=[11 * cm, 3 * cm, 4 * cm, 2 * cm])
        flowable_table.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 1, colors.black),
                                           ('FONT', (0,0), (-1,0), 'Times-Bold', 10, 12),
                                           ('FONT', (0,1), (-1,-1), 'Times-Roman', 10,12)]))

        flowables.append(flowable_table)
        flowables.append(PageBreak())
        found = 0
        if categories == "Commandes":
            found = 1
    if found == 0:
        print("The (Commandes) page has not been added! The category does not exist in the db.")
