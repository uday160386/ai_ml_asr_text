import cmudict

PROJECT_DATA_HOME="/home/kali/Documents/ai_ml/kaldi/egs/ex_kaldi_voice_text/s5"
TRAIN_DATA_HOME = "/home/kali/Documents/ai_ml/kaldi/egs/ex_kaldi_voice_text/s5/data/train/"
FLAC_HOME_FILES = PROJECT_DATA_HOME+"/audio_files/train_clean_100/"
# mod_root = PROJECT_DATA_HOME+"audio_files/train/wav/"
lexicon_temp_path = PROJECT_DATA_HOME+"/data/local/temp/lexicon.txt"
lexicon_file_path = PROJECT_DATA_HOME+"/data/local/dict/lexicon.txt"
nonsi = PROJECT_DATA_HOME+"/data/local/dict/nonsilence_phones.txt"


# bef_list=cmudict.dict_string()
# pa_dup={}

# for s in bef_list:
#     if s not in pa_dup:
#         pa_dup[s]=0

# with open(lexicon_temp_path, 'a') as f:
#     f.write(cmudict.dict_string())

# nonlex=[]
# with open(lexicon_temp_path, 'r') as in_file:
#     for line in in_file:
#         if line not in nonlex:
#             nonlex.append(line)  
#             print('added')
#         else:
#             print('not added:')
# print(nonlex)
# lex_dup=list(set(nonlex))

# with open(lexicon_file_path, 'a') as in_file:
#     for i in nonlex:
#         in_file.write(i)

nonsil=[]
with open(lexicon_file_path, 'r') as in_file:
    for line in in_file:
        a=line.split(' ')
        yr=a[1].replace('\n','')
        if yr not in nonsil:
            nonsil.append(yr)
print(nonsil)
dup=list(set(nonsil))

with open(nonsi, 'a') as in_file:
    for i in dup:
        in_file.write(i+'\n')