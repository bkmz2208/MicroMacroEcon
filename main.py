import import_data as imp_d
import export_data as exp_d
import copy
path = r"C:\Users\ILIY\Documents\KPI\3 course 5 semestr\MicroMacroEconom\MacroFin9"
# path = r'.\MacroFin9'
InputParams_out = 'InputParams_out.csv'
CashFlow_out = 'A CashFlow_out.csv'
InLGD_out = 'A In_LGD_out.csv'
PldValue_out = 'A PldValue_out.csv'
InputParams_in = 'InputParams.csv'
CashFlow_in = 'A CashFlow.csv'
InLGD_in = 'A In_LGD.csv'
PldValue_in = 'A PldValue.csv'



def operating_CashFlow(file_name):
    output = []
    NumSc_max = 4

    for row_file in range(len(file_name)):
        if file_name[row_file]['NumSc'] == '0':
            for i in range(NumSc_max):
                dict_row = copy.deepcopy(file_name[row_file])
                output.append(dict_row)
                output[len(output)-1]['NumSc'] = str(i)
        else:
            output.append(file_name[row_file])
    # output[0]['NumSc'] = str(1)

    return output

file = imp_d.read_to_dict_csv(CashFlow_in)
file_o = operating_CashFlow(file)
# file_oo = operating_CashFlow_2(file_o)
exp_d.write_to_csv(file_o, CashFlow_out)
# print(file[1,{'NumSc'}])
# print(file[0]['NumSc'])
# file[0]['NumSc']='1'
# print(file[0]['NumSc'])
# for row in file:
#     if file[row]{NumSc} == 0:
#         print(1)
# exp_d.write_to_csv(file, CashFlow_out)


def is_file_r(file):
    try:
        open(file, 'r')
        return True
    except:
        return False


def is_file_w(file):
    try:
        open(file, 'w')
        return True
    except:
        return False
