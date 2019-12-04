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

file = imp_d.read_to_dict_csv(CashFlow_in)


#add data + copied lines
def operating_CashFlow(file_name):
    # file_name_r = []
    file_name_r = copy.deepcopy(file_name)
    # for row in range(len(file_name)):
    #     file_name_r.append(file_name[row])
    output = []
    print(file_name)
    print(file_name_r)

    # output.append(file_name_r[0])
    # output.append(file_name_r[0])
    # output[1]['NumSc'] = str(1)

    for row in range(len(file_name)):
        output.append(file_name_r[row])
        if file_name_r[row]['NumSc'] == '0':
            for i in range(3):
                output.append(file_name_r[row])
                # output.append(file_name_r[row])
                # output[row+1]['NumSc'] = str(1)
            # output.append(file_name_r[row])
            # output[row+1]['NumSc'] = str(2)
            # output.append(file_name_r[row])
            # output[row+2]['NumSc'] = str(3)
            # output.append(file_name_r[row])
            # output[row+3]['NumSc'] = str(4)
    output[1]['NumSc'] = str(1)

    print(file_name)
    print(file_name_r)

    return output


def operating_CashFlow_2(file_name):
    # output = []
    output = copy.deepcopy(file_name)
    # print(output)
    # print('1234567890')
    for row in range(len(file_name)):
        # output.append(file_name_r[row])
        if file_name[row]['NumSc'] == '0':
            # for i in range(4):
                # output.append(file_name[row])
                # output.append(file_name_r[row])
            output[row+0]['NumSc'] = str(1)
    return output


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
