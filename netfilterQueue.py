from netfilterqueue import NetfilterQueue

def print_and_accept(pkt):
    print(pkt)
    pkt.drop()
    print('packet has been dropped')

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print('')

nfqueue.unbind()
