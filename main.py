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
exp_d.write_to_csv(file, CashFlow_out)

# def is_file_r(file):
#     try:
#         open(file, 'r')
#         return True
#     except:
#         return False


# def is_file_w(file):
#     try:
#         open(file, 'w')
#         return True
#     except:
#         return False
