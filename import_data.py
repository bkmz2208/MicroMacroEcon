import xlrd
import xlwt


# read data from xlsx
def read_to_dict_xl(file_name):
    rb = xlrd.open_workbook(file_name)
    sheet = rb.sheet_by_index(0)
    rows = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    headers = rows[0]

    output = []
    for row in rows[1:]:
        dict_row = {}
        for index, cell in enumerate(row):
            dict_row[headers[index]] = cell
        output.append(dict_row)

    return output


# read data from csv
def read_to_dict_csv(file):
    output = []
    with open(file, 'r') as file_in:
        columns_name = file_in.readline().replace('\n', '').split(';')
        row = file_in.readline().replace('\n', '').split(';')
        while len(row) > 1:
            dict_row = {}
            for index, name in enumerate(columns_name):
                dict_row[name] = row[index]
            output.append(dict_row)

            row = file_in.readline().replace('\n', '').split(';')
    return output

