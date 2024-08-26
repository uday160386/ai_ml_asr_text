import sys, os

PROJECT_HOME = "/home/kali/Documents/ai_ml/kaldi/egs/ex_kaldi_voice_text/s5"
PROJECT_DATA_HOME=PROJECT_HOME+"/data"
mod_root = PROJECT_HOME+"/audio_files/train/wav"
wav_scp_file_path = PROJECT_DATA_HOME+"/train/wav.scp"




for path, subdirs, files in os.walk(mod_root):
    for name in files:
        split_filename=name.split(".wav")
        get_sub_dir=split_filename[0].split('-')

        # adding index content to wav.scp
        with open(wav_scp_file_path, 'a') as file:
                file.write("{} {}\n".format(split_filename[0], mod_root+'/'+get_sub_dir[0]+'/'+get_sub_dir[1]+'/'+split_filename[0]+'.wav'))



print('Added content to wav.scp successfully.....')