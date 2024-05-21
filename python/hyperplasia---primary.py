# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"7702.0","system":"readv2"},{"code":"2627.0","system":"readv2"},{"code":"64296.0","system":"readv2"},{"code":"929.0","system":"readv2"},{"code":"7555.0","system":"readv2"},{"code":"35676.0","system":"readv2"},{"code":"5906.0","system":"readv2"},{"code":"16035.0","system":"readv2"},{"code":"3045.0","system":"readv2"},{"code":"N40","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hyperplasia-of-prostate-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hyperplasia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hyperplasia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hyperplasia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
