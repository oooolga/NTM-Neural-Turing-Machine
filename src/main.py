import random
from random import randint
from data_gen import CopyTaskGenerator
import ipdb, pdb
import torch
from models import LSTMBaselineCell
from models import NTMCell
from torch import optim
import argparse, os
import utils
import numpy as np
import os

parser = argparse.ArgumentParser("NTM Copy Task")
parser.add_argument("--model", default="mlp_ntm",
                    help="[baseline] | [lstm_ntm] | [mlp_ntm] ")

parser.add_argument("--batch-size", default=1)
parser.add_argument("--train-steps", default=50000, type=int,
                    help="number of train steps")
parser.add_argument("--print-freq", default=200)
parser.add_argument("--save-freq", default=2500, type=int)
parser.add_argument("--lr", default=1e-4, type=float)
parser.add_argument("--momentum", default=0.9, type=float)
parser.add_argument("--alpha", default=0.95, type=float)
parser.add_argument("--clip", default=5, type=float,
                    help="gradient clipping")

parser.add_argument("--M", default=20)
parser.add_argument("--N", default=128)
parser.add_argument("--controller-size", default=100)

parser.add_argument("--seq-dim", default=8, help="copy task input dim")
parser.add_argument("--max-seq-len", default=20, help="copy task input length")

parser.add_argument("--logdir", default="./mlpntm_logs", type=str, help="output log for plots")
parser.add_argument("--model-dir", default="./saved_models", type=str,
                    help="directory for saved models")
parser.add_argument('--model-prefix', default='mlpntm_', type=str,
                    help='output model name\'s prefix')
args = parser.parse_args()
use_cuda = torch.cuda.is_available()

if os.path.isdir(args.logdir):
    print("{} exists!".format(args.logdir))
    exit(0)
if not os.path.exists(args.model_dir):
    os.makedirs(args.model_dir)
##########################END OF ARGS###############################

# Copy Task
copy_task_gen = CopyTaskGenerator(
    max_seq_len=args.max_seq_len, seq_dim=args.seq_dim
)

model, optimizer = utils.get_model_optimizer(args, use_cuda)

print("{} has {} parameters".format(
    args.model, sum([np.prod(p.size()) for p in model.parameters() ])
))

criterion = torch.nn.BCELoss()
global_step = 0
loss_avg = 0
writer = utils.Logger(args.logdir)

# save heper params
hparams = []
args_dict = vars(args)
for key in args_dict.keys():
    hparams.append("{}: {}\n".format(key, args_dict[key]))
with open(os.path.join(args.logdir, "hparam.txt"), "w") as f:
    f.writelines(hparams)


model.train()
while global_step < args.train_steps:
    inp, target = copy_task_gen.generate_batch(batch_size=args.batch_size)
    pred = model(inp)

    optimizer.zero_grad()
    loss = criterion(pred, target)
    loss_avg += loss.data[0]
    loss.backward()

    for p in model.parameters():
        p.grad.data.clamp_(max=args.clip)

    optimizer.step()
    global_step += 1

    if global_step % args.print_freq == 0:
        print("at step {} loss {}".format(global_step, loss_avg / args.print_freq))
        writer.scalar_summary("train_bce", loss_avg / args.print_freq, global_step)
        loss_avg = 0

    if args.save_freq and global_step % args.save_freq == 0:
        utils.save_checkpoints({
            'global_step': global_step,
            'args': args,
            'state_dict': model.state_dict(),
            'optimizer': optimizer.state_dict()
            }, os.path.join(args.model_dir, args.model_prefix+str(global_step)+'.pt'))


