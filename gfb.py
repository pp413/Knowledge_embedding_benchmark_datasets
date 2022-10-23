import os
import argparse

arg = argparse.ArgumentParser()

arg.add_argument("--path", type=str)

args = arg.parse_args()

def generate_entity(path):

    files = ["FB15k_mid2name.txt", "FB15k_mid2description.txt"]
    
    to_files = ["ent2name.txt", "ent2text.txt"]
    
    for i in range(2):
        
        read = os.path.join(path, files[i])
        write = os.path.join(path, to_files[i])
        
        with open(read, "r", encoding="utf-8") as fr, open(write, "a", encoding="utf-8") as fw:
            
            for line in fr.readlines():
                
                if "name" in files[i]:
                    line = line.strip().split("\t")
                    line[1] = line[1].replace("_", " ").replace("-", " ")
                    fw.write("\t".join(line) + "\n")
                else:
                    line = line.strip().split("\t")
                    if line[1].endswith('."@en'):
                        line[1] = line[1][1:-4].replace("\\\"", "\"").replace("\\n", " ")
                    fw.write("\t".join(line) + "\n")
        

def generate_relation(path):
    
    read = os.path.join(path, "train.txt")
    write = os.path.join(path, "rel2text.txt")
    
    relations = set()
    
    with open(read, 'r', encoding='UTF-8') as fr:
        
        for line in fr.readlines():
            line = line.strip().split("\t")
            relations.add(line[1])
    
    with open(write, 'a', encoding='UTF-8') as fw:
        
        for line in list(relations):
            fw.write(line + "\t" + line.replace("_", " ").replace("/", " ")[1:] + "\n")




generate_entity(args.path)

generate_relation(args.path)





