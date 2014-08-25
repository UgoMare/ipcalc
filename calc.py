import ipcalc
import sys

args = sys.argv[1:]
i = 0
for ip1 in args:
    i = i + 1
    for ip2 in args[i:]:
        mask1 = int(ip1.split('/')[1])
        mask2 = int(ip2.split('/')[1])
        more_res = (mask2, mask1)[mask1 >= mask2]
        print "%s  &&  %s  == > %s" % (ip1, ip2, ("Don't Match", "Match !")[ipcalc.IP(ip1.split('/')[0]).bin()[0:more_res] == ipcalc.IP(ip2.split('/')[0]).bin()[0:more_res]])
