import os

def generate_name_text_for_wordnet(path):
    data_name = path.split('/')[-1]
    entity_name = []
    entity_text = []
    
    longtext_path = ''
    name_text_path = ''
    entity2text = ''
    entity2name = ''
    
    if data_name.lower().find('wn18') != -1:
        longtext_path = os.path.join(path, 'wordnet-mlj12-definitions.txt')
        entity2text = os.path.join(path, 'WN_entity2text.txt')
        entity2name = os.path.join(path, 'WN_entity2name.txt')
    else:
        return False
        
    with open(longtext_path, 'r', encoding='UTF-8') as fr:
        lines = fr.readlines()
        
        for line in lines:
            line = line.strip()
            temp = line.split('\t')
            if len(temp) == 3:
                if temp[1].find('_NN_') != -1 or temp[1].find('_JJ_') != -1 or temp[1].find('_VB_') != -1 or temp[1].find('_RB_') != -1:
                    wordnet_str = temp[1][2:]
                    num_start = wordnet_str.rfind('_')
                    pos_start = wordnet_str[:num_start].rfind('_')
                    name = wordnet_str[:pos_start]
                    name = name.replace('_', ' ')
                    entity_name.append(temp[0] + '\t' + name)
                    entity_text.append(temp[0]+ '\t' + name + ', ' + temp[2])
    
    with open(entity2name, 'w', encoding='UTF-8') as fw1, open(entity2text, 'w', encoding='UTF-8') as fw2:
        fw1.write('\n'.join(entity_name))
        fw2.write('\n'.join(entity_text))
    
    return True

def generate_name_text_for_freebase(path):
    data_name = path.split('/')[-1]
    entity_name = []
    entity_text = []
    
    longtext_path = ''
    name_text_path = ''
    entity2text = ''
    entity2name = ''
    
    if data_name.lower().find('fb15k') != -1:
        longtext_path = os.path.join(path, 'FB15k_mid2description.txt')
        name_text_path = os.path.join(path, 'FB15k_mid2name.txt')
        entity2text = os.path.join(path, 'FB_entity2text.txt')
        entity2name = os.path.join(path, 'FB_entity2name.txt')
    else:
        return False
        
    with open(longtext_path, 'r', encoding='UTF-8') as fr:
        lines = fr.readlines()
        
        for line in lines:
            line = line.strip()
            temp = line.split('\t')
            temp[1] = temp[1][1:-4]
            temp[1] = temp[1].replace('_', ' ')
            entity_text.append(temp[0]+ '\t' + temp[1])
    
    with open(name_text_path, 'r', encoding='UTF-8') as fr:
        lines = fr.readlines()
        
        for line in lines:
            line = line.strip()
            temp = line.split('\t')
            temp[1] = temp[1].replace('_', ' ')
            entity_name.append(temp[0] + '\t' + temp[1])
    
    with open(entity2name, 'w', encoding='UTF-8') as fw1, open(entity2text, 'w', encoding='UTF-8') as fw2:
        fw1.write('\n'.join(entity_name))
        fw2.write('\n'.join(entity_text))
    
    return True


def generate_text_for_relation_of_freebase(relations):
    relation_text = {}
    for relation in relations:
        relation_text[relation] = relation[1:].replace('/', ' ')
    return relation_text

def generate_text_for_relation_of_wordnet(relations):
    relation_text = {}
    for relation in relations:
        relation_text[relation] = relation[1:].replace('_', ' ')
    return relation_text

def load_text_from(path):
    data = {}
    with open(path, 'r', encoding='UTF-8') as fr:
        lines = fr.readlines()
        for line in lines:
            line = line.strip().split('\t')
            data[line[0]] = line[1]
    return data
    
    

if __name__ == '__main__':
    wn_path = os.path.join('WN18RR')
    fb_path = os.path.join('FB15k-237')
    generate_name_text_for_wordnet(wn_path)
    
    generate_name_text_for_freebase(fb_path)
    


