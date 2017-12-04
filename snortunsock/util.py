

def classifications(path="/usr/local/etc/snort/classification.config"):
    with open(path) as f:
        l = [x.rstrip("\r\n") for x in f.readlines() if x[0] != '#']
        l = [x.split(" ") for x in l if len(x) > 2]
        l = [x[2].split(',')[0] for x in l]
    return {k+1: v for k, v in enumerate(l)}

