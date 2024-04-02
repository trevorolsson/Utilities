import pandas as pd
import glob
import random
import os

def main():
    loaded = load()
    exclude = []
    groups = lab_group(loaded, exclude)
    export_group_list(groups)
    return

def load():
    try:
        data_all = pd.read_csv(glob.glob(f"*.{str('csv')}")[0], skiprows=[1], index_col=False)
    except IndexError:
        print(f'IndexError: Make sure path is correct. Current path is: {os.getcwd()}')
        exit()
    useful_keys = ["Student", "Section"]
    data = data_all[useful_keys]
    reorganized = data.groupby('Section').Student.apply(list).to_dict()
    return reorganized

def lab_group(dictionary:dict, exclude):
    
    groups = {key:[] for key in dictionary.keys()}
    number_of_groups = 8
    
    for section, students in dictionary.items():
        for student in students:
            if student in exclude:
                students.remove(student)
            else:
                pass

                
    for section, students in dictionary.items():
        
        random.shuffle(students)
        for _ in range(number_of_groups):
            group = []
            for _ in range(3):
                if students:
                    group.append(students.pop(0))
                else:
                    group.append(None)
            groups[section].append(group)
        
        if groups[section][-1].count(None) >=2:
            for idx in range(2):
                groups[section][-1].append(groups[section][idx].pop(-1))
                groups[section][-1].pop(0)
            groups[section][-1].append(groups[section][-1].pop(0))
                
    return groups

                               
def export_group_list(dictionary:dict):
    indices = [f"Group {idx+1}" for idx in range(8)]
    for section in dictionary.keys():
        df = pd.DataFrame(dictionary[section])
        df.to_csv(f'export/{section}_assignment.csv', header=False, index=indices)
    return

if __name__=="__main__":
    main()