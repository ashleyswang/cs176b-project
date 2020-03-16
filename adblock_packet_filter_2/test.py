from netfilterqueue import NetfilterQueue

def print_and_accept(pkt):
    print(pkt)
    print(pkt.get_payload())
    pkt.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print('')

nfqueue.unbind()
