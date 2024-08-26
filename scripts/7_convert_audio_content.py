import sys, os
import shutil

PROJECT_DATA_HOME="/home/kali/Documents/ai_ml/kaldi/egs/ex_kaldi_voice_text/s5"
TRAIN_DATA_HOME = "/home/kali/Documents/ai_ml/kaldi/egs/ex_kaldi_voice_text/s5/data/train/"
FLAC_HOME_FILES = PROJECT_DATA_HOME+"/audio_files/train_clean_100/"
# mod_root = PROJECT_DATA_HOME+"audio_files/train/wav/"

# spk2utt_file_path = TRAIN_DATA_HOME+"spk2utt"
# spk_file_path = TRAIN_DATA_HOME+"spk"
utt_file_path = TRAIN_DATA_HOME+"utt.txt"

group_by_speaker={}
for path, subdirs, files in os.walk(FLAC_HOME_FILES):
    for name in files:
        if '.txt' in name:
            split_filename=name.split(".txt")
            get_sub_dir=split_filename[0].split('-')
            
            # converting data to .text files
            
            with open(FLAC_HOME_FILES+get_sub_dir[0]+'/'+get_sub_dir[1].split('.')[0]+'/'+name, 'r') as in_file:
                # open(txt_file_path, 'a') as text_out_file:
                for line in in_file:
                    # text_out_file.write("{}".format(line))
                    if get_sub_dir[0] in group_by_speaker:
                        group_by_speaker[get_sub_dir[0] ]=group_by_speaker.get(get_sub_dir[0])+ line.split(' ',1)[1]
                    else:
                        group_by_speaker[get_sub_dir[0] ]=line.split(' ',1)[1]

# # writing content to spk2utt
# with open(spk2utt_file_path, 'a') as spk2utt_out_file, \
#      open(spk_file_path,'a') as spk_out_file:
#     for key in group_by_speaker:
#         spk2utt_out_file.write("{} {}\n".format(key, group_by_speaker.get(key)))
#         spk_out_file.write("{}\n".format(key))     

unique_utternace_id={}
for key in group_by_speaker:
    word_arr = group_by_speaker[key].split(' ')
    for i in range(len(word_arr)):
        unique_utternace_id[word_arr[i].replace('\n',' ')]=''

# writing content to utt file
key_exists ={}
with open(utt_file_path, 'a') as utt_out_file:
    for key in unique_utternace_id:
        if key not in key_exists:
            utt_out_file.write("{}\n".format(key))  

print('text file content copied sucussfully.....')