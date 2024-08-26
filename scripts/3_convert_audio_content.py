import sys, os
import shutil

PROJECT_HOME = "/home/kali/Documents/ai_ml/kaldi/egs/ex_kaldi_voice_text/s5"
PROJECT_DATA_HOME = PROJECT_HOME+"/data/train"
FLAC_HOME_FILES = PROJECT_HOME+"/audio_files/train_clean_100/"
WAV_HOME_FILES = PROJECT_HOME+"/audio_files/train/wav/"
txt_file_path = PROJECT_DATA_HOME+"/text"
corpus_file_path = PROJECT_HOME+"/data/local/dict/corpus.txt"

group_by_speaker={}
for path, subdirs, files in os.walk(FLAC_HOME_FILES):
    for name in files:
        if '.txt' in name:
            split_filename=name.split(".txt")
            get_sub_dir=split_filename[0].split('-')
            
            # converting data to .text files
            
            with open(FLAC_HOME_FILES+get_sub_dir[0]+'/'+get_sub_dir[1].split('.')[0]+'/'+name, 'r') as in_file, \
                open(txt_file_path, 'a') as text_out_file, \
                open(corpus_file_path, 'a') as corpos_out_file:
                for line in in_file:
                    text_out_file.write("{}".format(line))
                    temp=line.split(' ')
                    temp2=' '.join(temp[1:])
                    corpos_out_file.write("{}".format(temp2))
                    if get_sub_dir[0] in group_by_speaker:
                        group_by_speaker[get_sub_dir[0] ]=group_by_speaker.get(get_sub_dir[0])+ line.split(' ',1)[1]
                    else:
                        group_by_speaker[get_sub_dir[0] ]=line.split(' ',1)[1]
