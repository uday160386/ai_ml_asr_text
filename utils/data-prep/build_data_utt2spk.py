import sys, os
import shutil

TRAIN_DATA_HOME = "/home/kali/Documents/ai_ml/kaldi/egs/ex_kaldi_voice_text/s5/data/train/"
FLAC_HOME_FILES = TRAIN_DATA_HOME+"audio_files/train_clean_100/"
mod_root = TRAIN_DATA_HOME+"audio_files/wav"
utt2spk_file_path = TRAIN_DATA_HOME+"utt2spk"

for path, subdirs, files in os.walk(mod_root):
    for name in files:
        if '.wav' in name:
            split_filename=name.split(".wav")
            get_sub_dir=split_filename[0].split('-')
            
            # converting data to .text files
            
            with open(utt2spk_file_path, 'a') as text_out_file:
                text_out_file.write("{} {}\n".format(get_sub_dir[0], name))
            

print('utt2spk file content updated sucussfully.....')