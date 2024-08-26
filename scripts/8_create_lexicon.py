from indic_unified_parser.uparser import wordparse
split_word = set()

PROJECT_DATA_HOME="/home/kali/Documents/ai_ml/kaldi/egs/ex_kaldi_voice_text/s5"
TRAIN_DATA_HOME = "/home/kali/Documents/ai_ml/kaldi/egs/ex_kaldi_voice_text/s5/data/train/"
FLAC_HOME_FILES = PROJECT_DATA_HOME+"/audio_files/train_clean_100/"
# mod_root = PROJECT_DATA_HOME+"audio_files/train/wav/"
lexicon_file_path = PROJECT_DATA_HOME+"/data/local/dict/lexicon.txt"
# spk2utt_file_path = TRAIN_DATA_HOME+"spk2utt"
# spk_file_path = TRAIN_DATA_HOME+"spk"
utt_file_path = TRAIN_DATA_HOME+"utt.txt"

key_exists ={}
with open(utt_file_path, 'r') as f:
    with open(lexicon_file_path, 'w') as o:
        lines = f.readlines()
        
        for line in lines:
            line = line.strip()
            if line not in key_exists:
                parsed_output_string = wordparse(line, 0, 1, 1)
                o.write(f'{line}\t{parsed_output_string}\n')