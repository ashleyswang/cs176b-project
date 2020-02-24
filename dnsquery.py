import dns
import dns.resolver
import dns.reversename

result = dns.reversename.from_address('64.68.90.1')
print(result)
print(dns.reversename.to_address(result))
