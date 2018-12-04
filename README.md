# Neural Graph to Sequence Model

This repository contains the code for our paper [A Graph-to-Sequence Model for AMR-to-Text Generation](https://arxiv.org/abs/1805.02473) in ACL 2018

The code is developed under TensorFlow 1.4.1. 
We shared our pretrained model along this repository. 
Due to the compitibility reason of TensorFlow, it may not be loaded by some lower version (such as 1.0.0).

Please create issues if there are any questions! This can make things more tractable. 

## Release of 2M automatically parsed data (Dec. 4th, 2018)
I realize that releasing our 2M data can be helpful for others, thus we release the data, which can be downloaded from [here](https://www.cs.rochester.edu/~lsong10/downloads/2m.json)

## Data precrocessing
Our current data loading [code](./src_g2s/G2S_data_stream.py) requires simplified AMR graphs where variable tags, sense tags and quotes are removed. For example, the following AMR
```
(d / describe-01 
    :ARG0 (p / person 
        :name (n / name 
            :op1 "Ryan")) 
    :ARG1 p 
    :ARG2 genius)
```
need to be first converted into a single line, before being simplified as
```
describe :arg0 ( person :name ( name :op1 ryan )  )  :arg1 person :arg2 genius
```
Given an original AMR corpus (the [AMR website@ISI](https://amr.isi.edu/download.html) contains several datasets, one example is the [little prince](https://amr.isi.edu/download/amr-bank-struct-v1.6.txt)). First, to make each AMR into a single line, here I release my [script](./AMR_multiline_to_singleline.py) for doing it, you may need to further modify it for your dataset. Second, to simplify single-line AMRs, we release our simplifier, which can be downloaded [here](https://www.cs.rochester.edu/~lsong10/downloads/amr_simplifier.tgz). It is generated by modifying the [NeuralAMR](https://github.com/sinantie/NeuralAmr) code.

Here we briefly introduce how to use our simplifier. 
First make sure that each AMR takes exactly one line in your file. 
We have the 
For example, you have a file 'demo.amr', which contains
```
(d / describe-01 :ARG0 (p / person :name (n / name :op1 "Ryan")) :ARG1 p :ARG2 genius)
```
Then, simply execute 
```
./anonDeAnon_java.sh anonymizeAmrFull true demo.amr
```
and the program will generate file 'demo.amr.anonymized', which contains the simplified AMRs.
Please note that our simplifier *does not* do anonymization, which is introduced by [NeuralAMR](https://github.com/sinantie/NeuralAmr) (Konstas et al., 2017). The resulting file name has 'anonymized' because our simplifier is obtained by modifying NeuralAMR. We actually don't do anonymization.

Another alternative is to write your own data loading code according to the format of your own AMR data. 

### Input data format
After simplifying AMRs, you can merge them with the corresponding sentences into a JSON file, which is the input data format for our system, the following sample below demonstrates one case:
```
[{"amr": "describe :arg0 ( person :name ( name :op1 ryan )  )  :arg1 person :arg2 genius",
"sent": "ryan's description of himself: a genius.",
"id": "demo"}]
```
In general, the JSON file contains a list of instances, and each instance is a dictionary with fields of "amr", "sent" and "id"(optional).

### Vocabulary extraction
After having the JSON files, you can extract vocabularies with our released scripts in the [data](./data/) sub-directory.
We also encourage you to write your own scripts.

## Training

First, modify the PYTHONPATH within [train_g2s.sh](./train_g2s.sh) (for our graph-to-string model) or [train_s2s.sh](./train_s2s.sh) (for baseline). <br>
Second, modify config_g2s.json or config_s2s.json. You should pay attention to the field "suffix", which is an identifier of the model being trained and saved. We usually use the experiment setting, such as "bch20_lr1e3_l21e3", as the identifier. <br>
Finally, execute the corresponding script file, such as "./train_g2s.sh".

### Using large-scale automatic AMRs

In this setting, we follow [Konstas et al., (2017)](https://arxiv.org/abs/1704.08381) to take the large-scale automatic data as the training set, with the original gold data being the finetune set. To train in this way, you need add a new field "finetune_path" in the configuration file and point it to the gold data. Then, point "train_path" to the automatic data. 

For training on the gold data only, we use an initial learning rate of 1e-3 and L2 normalization of 1e-3. We then lower the learning rate to be 8e-4, 5e-4 and 2e-4 after a number of epoches. 

For training on both gold and automatic data, the initial learning rate and L2 normalization are 5e-4 and 1e-8. We also lower the learning rate during training. 

The idea of lowering learning rate was first introduced by Konstas et al., (2017).


## Decoding with a pretained model

Simply execute the corresponding decoding script with one argument being the identifier of the model you want to use.
For instance, you can execute "./decode_g2s.sh bch20_lr1e3_l21e3"

### Pretrained model

We releaes our recently pretrained model using gold plus 2M automatically-parsed AMRs [here](https://www.cs.rochester.edu/~lsong10/downloads/model_silver_2m.tgz). With this model, we observed a BLEU of *33.6*, which is higher than our paper-reported number of 33.0. The pretrained model with only gold data is [here](https://www.cs.rochester.edu/~lsong10/downloads/model_gold.tgz). It reports a test BLEU score of 23.3.

## Cite
If you like our paper, please cite
```
@InProceedings{song-EtAl:acl2018,
  author    = {Song, Linfeng  and  Zhang, Yue  and  Wang, Zhiguo  and  Gildea, Daniel},
  title     = {A Graph-to-Sequence Model for {AMR}-to-Text Generation},
  booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (ACL-18)},
  year      = {2018},
  address   = {Melbourne, Australia},
}
```
