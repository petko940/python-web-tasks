# https://www.codewars.com/kata/526989a41034285187000de4/train/python

def ips_between(start, end):
    def ip_count(ip):
        octets = ip.split('.')
        return (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])

    start = ip_count(start)
    end = ip_count(end)

    return end - start
