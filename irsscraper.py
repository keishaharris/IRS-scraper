import requests
from bs4 import BeautifulSoup
import os
import json

def make_soup(url):
    html_content = requests.get(url)
    html_content.raise_for_status()
    parser = BeautifulSoup(html_content.text, 'html.parser')
    return parser

def find_table(soup):
    table = soup.find("table", class_="picklist-dataTable")
    table_rows = table.find_all('tr')[1:]
    return table_rows

def check_key_value(value, array): 
    for i, v in enumerate(array):
            if v["form_number"] == value:
                return True
            
def save_as_pdf(form_number, pdf, form_year):

        dir_name= str(form_number)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        res = requests.get(pdf)
        with open(f'{dir_name}/{form_number} - {form_year}.pdf', 'wb') as f:
            f.write(res.content)
  
def main():
    textfile_results = []

    MIN_RANGE = 2018
    MAX_RANGE = 2020

    with open('test.txt') as f:
        textfile_results = [line.rstrip() for line in f]

    for results in textfile_results:
        format = results.split()
        url = f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=0&criteria=formNumber&value={format[0]}+{format[1]}&isDescending=false'

         #retrieves html content and creates parser
        soup = make_soup(url)

        #retrieves rows within table data
        table_rows = find_table(soup) 

        tax_forms=[]

        #FIRST UTILITY
        for row in table_rows: 
            form_number = row.find('td', 'LeftCellSpacer').text.strip()
            if form_number == results:
                form_title = row.find('td', 'MiddleCellSpacer').text.strip()
                form_year = int(row.find('td', 'EndCellSpacer').text.strip())
                res = check_key_value(value=form_number, array = tax_forms) #Checks if respective form number value exists
                if (res):
                    if form_year < tax_forms[0]["min_year"]:
                        tax_forms[0]["min_year"] = form_year
                    elif form_year > tax_forms[0]["max_year"]:
                        tax_forms[0]["max_year"] = form_year
                else:
                    tax_forms.append({
                        "form_number":form_number,
                        "form_title":form_title,
                        "min_year": form_year,
                        "max_year": form_year
                        })
                
                if MIN_RANGE <= form_year <= MAX_RANGE:
                    for link in row.find_all('a'):
                            pdf = link.get('href')

                    #SECOND UTILITY
                    data = save_as_pdf(pdf=pdf,form_number=form_number,form_year=form_year) 
        final_results = json.dumps(tax_forms)
        print(final_results)

if __name__ == '__main__':
    main()