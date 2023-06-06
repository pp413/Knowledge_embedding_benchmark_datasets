import os

import argparse

arg = argparse.ArgumentParser()

arg.add_argument("--path", type=str)

args = arg.parse_args()

def generate_entity(path):

    files = "wn-entity2text-new.txt"
    to_files = "ent2text.txt"
        
    read = os.path.join(path, files)
    write = os.path.join(path, to_files)
    
    with open(read, "r", encoding="utf-8") as fr, open(write, "a", encoding="utf-8") as fw:
        
        for line in fr.readlines():
            
            line = line.replace(" -- ", ", ").strip().split("\t")
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
            fw.write(line + "\t" + line.replace("_", " ")[1:] + "\n")




generate_entity(args.path)

generate_relation(args.path)





