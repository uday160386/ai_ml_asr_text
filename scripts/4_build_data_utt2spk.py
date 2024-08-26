import sys, os
import shutil

PROJECT_HOME = "/home/kali/Documents/ai_ml/kaldi/egs/ex_kaldi_voice_text/s5"
PROJECT_DATA_HOME=PROJECT_HOME+"/data/train/"
FLAC_HOME_FILES = PROJECT_HOME+"/audio_files/train_clean_100/"
WAV_FILES = PROJECT_HOME+"/audio_files/train/wav"
utt2spk_file_path = PROJECT_DATA_HOME+"utt2spk"

for path, subdirs, files in os.walk(WAV_FILES):
    for name in files:
        if '.wav' in name:
            split_filename=name.split(".wav")
            get_sub_dir=split_filename[0].split('-')
            
            # converting data to .text files
            
            with open(utt2spk_file_path, 'a') as text_out_file:
                text_out_file.write("{} {}\n".format(name.replace('.wav',''),get_sub_dir[0]))
            

print('utt2spk file content updated sucussfully.....')