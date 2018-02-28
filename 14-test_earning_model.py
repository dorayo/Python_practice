#!/usr/bin/env python3

import random
from termcolor import *

random.seed()

# 投入资本
total = 400.0
# 调节资本
adjust = 600.0
back = 0.0
forward = 0.0
count = 0

while total > 1.0 and count < 100 and total+adjust < 2000:
    if random.random() <= 0.3:
        total = 0.9 * total
        back = 0.4 * total
        adjust = adjust + back
        print(colored('[-] back:    %7.2f total: %7.2f   adjust: %7.2f' % (back, total, adjust), 'green'))
    else:
        forward = 0.6 * adjust
        total = 1.1 * total
        adjust = adjust - forward
        print(colored('[+] forward: %7.2f total: %7.2f   adjust: %7.2f' % (forward, total, adjust), 'red'))
    count = count + 1

if count >= 100:
    print(colored('time limited!', 'cyan'))
else:
    print(colored('count: %d' % count, 'cyan'))
print(colored('$Total: %d \n$Adjust: %d' % (total, adjust), 'yellow'))
