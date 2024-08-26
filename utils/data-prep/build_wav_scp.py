import sys, os

TRAIN_DATA_HOME = "/home/kali/Documents/ai_ml/kaldi/egs/ex_kaldi_voice_text/s5/data/train/"
mod_root = TRAIN_DATA_HOME+"audio_files/wav"
wav_scp_file_path = TRAIN_DATA_HOME+"wav.scp"

for path, subdirs, files in os.walk(mod_root):
    for name in files:
        split_filename=name.split(".wav")
        get_sub_dir=split_filename[0].split('-')

        # adding index content to wav.scp
        with open(wav_scp_file_path, 'a') as file:
                file.write("{} {}\n".format(split_filename[0], mod_root+'/'+get_sub_dir[0]+'/'+get_sub_dir[1]+'/'+split_filename[0]+'.wav'))



print('Added content to wav.scp successfully.....')