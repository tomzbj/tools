import csv

csvfile = open('pcp_rep.rpt')
reader = csv.reader(csvfile)
csvfile2 = open('__pcp_rep_jlc.csv', 'w', newline='\n')
writer = csv.writer(csvfile2, dialect='excel') 

reader = list(reader)

# 删除前五行
del reader[0:5]

# 按JLC的格式修改表头
line = ['Designator', 'Comment', 'Footprint', 'Mid X', 'Mid Y', 'Rotation', 'Layer'] 
print(line)
writer.writerow(line)

# 查找替换表, 请按需自行修改
footprint_table = {
    'CAPC1005': 'C0402',
    'CAPC1608': 'C0603',
    'CAPC2012': 'C0805',
    'CAPC3216': 'C1206',
    'CAPC3225': 'C1210',
    'DFN200P1100X1100-10': 'DFN10',
    'DIOM2012': 'D0805',
    'DIOM2716': 'LL-34',
    'DIOM5326': 'DO-214AC',
    'DIOM5436': 'SMB',
    'DIOM7959': 'SMC',
    'HC49SMD': 'HC49SMD',
    'INDC1005': 'L0402',
    'INDC1608': 'L0603',
    'INDC2012': 'L2012',
    'INDC3225': 'L1210',
    'INDC5050': 'L5040',
    'INDC7070': 'L7050',
    'INDC8080': 'L8050',
    'LEDC2012': 'LED0805',
    'LEDC1608': 'LED0603',
    'OSCCC250X320X100': 'SMD-3225',
    'OSCCC250X320X100A': 'SMD-3225',
    'OSCCC250X320X110': 'SMD-3225',
    'OSCCC320X500X110': 'SMD-5032',
    'OSCCC320X500X150': 'SMD-5032',
    'OSCSF320X150X080-2': 'SMD-3215',
    'OSCSF500X320X130-2': 'SMD-5032',
    'QFN40P300X300X85-21': 'QFN-20',
    'QFN50P400X400X80-21W5': 'QFN-20',
    'QFN50P500X500X100-29A': 'QFN-28',
    'QFN50P500X500X80-33W4': 'QFN-32',
    'QFN80P300X500-14V': 'QFN-14',
    'QFN80P400X300X80-9W': 'QFN-8',
    'QFN80P700X700X100-29V': 'QFN-28',
    'RESC1005': 'R0402',
    'RESC1608': 'R0603',
    'RESC2012': 'R0805',
    'RESC3216': 'R1206',
    'RESC6432': 'R2512',
    'RESCA2V80P160X320X70-8': 'R0603*4',
    'SOIC127P1028X265-20': 'SOIC-20',
    'SOIC127P1030X265-16': 'SOIC-16',
    'SOIC127P1030X265-18': 'SOIC-18',
    'SOIC127P1030X265-28': 'SOIC-28',
    'SOIC127P600X145-14': 'SOIC-14',
    'SOIC127P600X150-16': 'SOIC-16',
    'SOIC127P600X175-16': 'SOIC-16',
    'SOIC127P600X175-8': 'SOIC-8',
    'SOIC127P600X175-9': 'SOIC-8',
    'SOIC127P600X175-9A': 'SOIC-8',
    'SOIC127P700X210-16': 'SOIC-16',
    'SOIC127P760X203-8': 'SOIC-8',
    'SOIC127P780-8': 'SOIC-8',
    'SOIC127P787X213-8': 'SOIC-8', 
    'SOIC254P700X200-4': 'SOP-4_P2.54',
    'SOIC510P1005X320-4': 'DBS',
    'SOP127P680-4': 'SOIC-4',
    'SOP127P780X180-22': 'SOIC-22',
    'SOP65P778-20': 'TSSOP-20',
    'SOP65P780X200-28A': 'TSSOP-28',
    'SOT223': 'SOT-223',
    'SOT23-5': 'SOT23-5',
    'SOT23-6': 'SOT-23-6',
    'SOT23': 'SOT-23',
    'SOT23X': 'SOT-23',
    'SOT89-5': 'SOT-89-5',
    'SOT89': 'SOT-89',
    'TO252': 'TO-252-2',
    'TO263-2L': 'TO-263-2',
    'TO263-3L': 'TO-263-3',
    'TO263-5l': 'TO-263-5',
    'TQFP80P1600X1600X120-64': 'LQFP-64',
    'TQFP80P900X900X120-32': 'LQFP-32',
    'TSOP65P491X111-8': 'TSSOP-8',
    'TSOP65P640X110-28': 'TSSOP-28',
    'TSOP65P640X120-14': 'TSSOP-14',
    'TSOP65P640X120-16': 'TSSOP-16',
    'TSOP65P640X120-20': 'TSSOP-20',
    'TSOP65P640X120-24': 'TSSOP-24',
    'TSOP65P640X120-8': 'TSSP-8',
    'TSQFP50P1200X1200X160-64': 'LQFP-64',
    'TSQFP50P1600X1600X160-100': 'LQFP-100',
    'TSQFP50P900X900X145-48': 'LQFP-48',
    'TSSOP50P490X110-10A': 'TSSOP-10',
    'TSSOP50P810X110-48': 'TSSOP-48'
}

reader.sort(key = lambda x:x[2])

for line in reader:
    del line[1], line[2]        # 删除不需要的两列
    line[6] = 'T' if line[6] == 'NO' else 'B'
    if line[2] in footprint_table.keys():
        line[2] = footprint_table[line[2]]
    print(line) 
    writer.writerow(line)

csvfile.close() 
csvfile2.close() 
