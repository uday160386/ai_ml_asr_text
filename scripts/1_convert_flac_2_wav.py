import sys, os
import shutil

PROJECT_HOME = "/home/kali/Documents/ai_ml/kaldi/egs/ex_kaldi_voice_text/s5"
FLAC_HOME_FILES = PROJECT_HOME+"/audio_files/train_clean_100/"
WAV_FILES_HOME = PROJECT_HOME+"/audio_files/train/wav"

for path, subdirs, files in os.walk(FLAC_HOME_FILES):
    for name in files:
        if '.flac' in name:
            split_filename=name.split(".flac")
            get_sub_dir=split_filename[0].split('-')
            if not os.path.exists(WAV_FILES_HOME+"/"+get_sub_dir[0]+'/'+get_sub_dir[1]):
                os.makedirs(WAV_FILES_HOME+"/"+get_sub_dir[0]+"/"+ get_sub_dir[1])

            # converting data to .wav files
            shutil.copyfile(FLAC_HOME_FILES+get_sub_dir[0]+'/'+get_sub_dir[1]+'/'+name,
            WAV_FILES_HOME+"/"+get_sub_dir[0]+'/'+get_sub_dir[1]+'/'+split_filename[0]+'.wav' ) 

print('Files converted to WAV sucussfully.....')