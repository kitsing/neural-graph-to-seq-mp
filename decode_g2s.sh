#!/bin/bash
#SBATCH --partition=gpu --gres=gpu:1 -C K80 --time=1:00:00 --output=decode.out --error=decode.err
#SBATCH --mem=10GB
#SBATCH -c 6

export PYTHONPATH=$PYTHONPATH:${PWD}
export CUDA_VISIBLE_DEVICES=0

python src_g2s/G2S_beam_decoder.py --model_prefix logs_g2s/G2S.$1 \
        --in_path data/test.json \
        --out_path logs_g2s/test.g2s.$1\.tok \
        --mode beam

