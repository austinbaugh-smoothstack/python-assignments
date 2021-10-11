#!/bin/python3
import os, sys, logging, openpyxl

def main():
    logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
    # Parse CLI
    expected_format = "Expected input file format: expedia_monthly_<month>_<year>.xlsx"
    if len(sys.argv) != 2:
        logging.error("usage: ./" + sys.argv[0] + " <input-file-path>")
        logging.error(expected_format)
        return
    # Parse file path
    file_path = sys.argv[1]
    file_name = os.path.basename(file_path)
    prefix = "expedia_report_monthly_"
    suffix = ".xlsx"
    if not file_name.startswith(prefix) or not file_name.endswith(suffix):
        logging.error(expected_format)
        return
    date = file_name[len(prefix):-len(suffix)].split("_")
    if len(date) != 2:
        logging.error(expected_format)
        return
    month = date[0].title()
    year = int(date[1])
    logging.info("Date: " + month + ", " + str(year))

    wb = openpyxl.load_workbook(file_path)
    # Read sheet 1
    sheet1 = wb["Summary Rolling MoM"]
    for row in range(2, 14):
        row_date = sheet1.cell(row,column=1).value
        if row_date.strftime("%B") == month and row_date.year == year:
            for col in range(2, 7):
                label = sheet1.cell(row=1, column=col).value
                value = sheet1.cell(row, column=col).value
                logging.info(label + " : " + str(value * 100) + "%")
            break
    # Read sheet 2
    sheet2 = wb["VOC Rolling MoM"]
    col = 2
    while True:
        col_date = sheet2.cell(row=1,column=col).value
        if col_date.strftime("%B") == month and col_date.year == year:
            for row in range(3, 19):
                label = sheet2.cell(row, column=1).value
                value = sheet2.cell(row, column=col).value
                if label == None:
                    continue
                logging.info(label + " : " + str(value * 100) + "%")
            break
        col += 1


if __name__ == "__main__":
    main()
