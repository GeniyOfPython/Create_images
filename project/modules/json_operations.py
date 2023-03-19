import json
import modules.find_path as m_path
import modules.register as m_reg

base = {}

def write_json(filename):
    with open(m_path.find_path_to_file(filename), "w") as file:
        json.dump(base, file, indent = 4, ensure_ascii=True)
        

def read_json(filename):
    with open(m_path.find_path_to_file(filename), "r") as file:
        data = json.load(file)
        return data