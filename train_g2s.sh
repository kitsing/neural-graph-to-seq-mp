#!/bin/bash
#SBATCH -J g_2m -C K80 --partition=gpu --gres=gpu:1 --time=5-00:00:00 --output=train.out --error=train.err
#SBATCH --mem=80GB
#SBATCH -c 5

export PYTHONPATH=$PYTHONPATH:${PWD}
export CUDA_VISIBLE_DEVICES=0

python src_g2s/G2S_trainer.py --config_path ./config_g2s.json

