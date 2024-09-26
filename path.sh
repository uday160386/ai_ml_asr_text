export KALDI_ROOT=/home/uday/Documents/workspace/kaldi
export PATH=$PWD/utils/:$KALDI_ROOT/tools/openfst/bin:$PWD:$PATH
[ ! -f $KALDI_ROOT/tools/config/common_path.sh ] && echo >&2 "The standard file $KALDI_ROOT/tools/config/common_path.sh is not present -> Exit!" && exit 1
. $KALDI_ROOT/tools/config/common_path.sh
export LC_ALL=C
export DATA_ROOT="$KALDI_ROOT/egs/ai_ml_asr_text/audio_files/train"
# we use this both in the (optional) LM training and the G2P-related scripts
PYTHON='python2.7'

### Below are the paths used by the optional parts of the recipe

# We only need the Festival stuff below for the optional text normalization(for LM-training) step
FEST_ROOT=tools/festival
NSW_PATH=${FEST_ROOT}/festival/bin:${FEST_ROOT}/nsw/bin
export PATH=$PATH:$NSW_PATH
export IRSTLM="$KALDI_ROOT/tools/irstlm"


# SRILM is needed for LM model building
SRILM_ROOT=$KALDI_ROOT/tools/srilm
#SRILM_PATH=$SRILM_ROOT/sbin:$SRILM_ROOT/sbin/smp
export PATH=$PATH:$SRILM_PATH

export SRILM=$KALDI_ROOT/tools/srilm
# Sequitur G2P executable
sequitur=$KALDI_ROOT/tools/sequitur-g2p/g2p.py
sequitur_path="$(dirname $sequitur)/lib/$PYTHON/site-packages"

# Directory under which the LM training corpus should be extracted
LM_CORPUS_ROOT=./lm-corpus

