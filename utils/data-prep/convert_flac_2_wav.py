import sys, os
import shutil

TRAIN_DATA_HOME = "/home/kali/Documents/ai_ml/kaldi/egs/ex_kaldi_voice_text/s5/data/train/"
FLAC_HOME_FILES = TRAIN_DATA_HOME+"audio_files/train_clean_100/"
mod_root = TRAIN_DATA_HOME+"audio_files/wav"

for path, subdirs, files in os.walk(FLAC_HOME_FILES):
    for name in files:
        if '.flac' in name:
            split_filename=name.split(".flac")
            get_sub_dir=split_filename[0].split('-')
            if not os.path.exists(mod_root+"/"+get_sub_dir[0]+'/'+get_sub_dir[1]):
                os.makedirs(mod_root+"/"+get_sub_dir[0]+"/"+ get_sub_dir[1])

            # converting data to .wav files
            shutil.copyfile(FLAC_HOME_FILES+get_sub_dir[0]+'/'+get_sub_dir[1]+'/'+name,
            mod_root+"/"+get_sub_dir[0]+'/'+get_sub_dir[1]+'/'+split_filename[0]+'.wav' ) 

print('Files converted to WAV sucussfully.....')