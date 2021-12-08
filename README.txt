IRS SCRAPER 

A tool used to search through IRS product forms and retrieve Product Form Data. The program will return the product name, title, min and max years as well as create a sub-directory within current directory and download pdf file of the product. 

Installation:

Download zip file to hard drive. Zip file contains this README, python file and a text file containg a list of Form Names. This text file can be altered by adding or removing desired Tax Forms. 

Libraries Used:
Python Version - 3.9.5

Request - pip install requests
Beauitufl Soup - pip install beautifulsoup4
JSON - pip install jsons

Usage:
Once downloaded, program can start by moving into the unzipped directory in the terminal and then calling the python file in this format:

python3 irsscraper.py

The script will then run and the first utitlity will perform its function. It will return a JSON strucutred format of the product name, product title and minimum and maxium year of each tax form listed inside of the text file. 

The second utility will run and use the data from the previous function to compare if the product's year is within the hardcoded min and max range. If so, the script will create a sub-directory within the zip file and download the pdf content into the sub-folder.

This was an awesome challenge and definitely stretched my learnings. I have briefly played with Beautiful Soup so it was nice being able to translate my learnings into a real world applicable problem. Thanks for giving me the opportunity! 