import sys, os
import shutil

PROJECT_HOME = "/home/kali/Documents/ai_ml/kaldi/egs/ex_kaldi_voice_text/s5"
PROJECT_DATA_HOME = PROJECT_HOME+"/data/local/dict"
lexicon_file_path = PROJECT_DATA_HOME+"/lexicon.txt"
non_silence_file_path = PROJECT_DATA_HOME+"/nonsilence_phones.txt"

with open(lexicon_file_path, 'r') as in_file, \
open(non_silence_file_path, 'a') as text_out_file:
                for line in in_file:
                    nonsi = line.split('  ')
                    if len(nonsi) >1:
                        text_out_file.write("{}".format(nonsi[1]))
                    else:
                        text_out_file.write("{}".format(nonsi[0]))
