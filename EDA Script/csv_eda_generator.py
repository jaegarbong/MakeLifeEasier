"""

"""

from pandas import read_csv
from ydata_profiling import ProfileReport
from os import getcwd, listdir, path,makedirs


file_list = listdir(getcwd())
csv_files = [filename for filename in file_list if filename.endswith('.csv')]
    

eda_report_folder = path.join(getcwd(),"EDA Reports")
if not path.exists(eda_report_folder):
    makedirs(eda_report_folder)

for filename in csv_files:
    file_path = path.join(getcwd(),filename)
    data = read_csv(file_path)

    profile = ProfileReport(data)
    report_filepath = path.join(eda_report_folder,filename.replace(".csv","_report.html"))
    profile.to_file(report_filepath)    
