
def write_to_csv(data, output_name):
    # if open(output_name):
    #     output_name.closefile()
    with open(output_name, 'w') as file_out:
        row_names = data[0].keys()
        file_out.write(';'.join(row_names))
        file_out.write('\n')

        for row in data:
            file_out.write(';'.join(row.values()))
            file_out.write('\n')

