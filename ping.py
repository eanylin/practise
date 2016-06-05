#!/usr/bin/python -tt

import subprocess
import sys

def print_ip(filename):
  f = open(filename, 'r')
  ip_list = f.read()
  print ip_list,
  f.close()


def ping_ip(filename):
  f = open(filename, 'r')
  ip_list = f.read().splitlines()
  reachable_ip = []
  non_reachable_ip = []

  print "Performing Ping Tests..."

  for ip in ip_list:
    result = []
    process = subprocess.Popen(['ping', '-c', '1', '-n', '-W', '5', ip], shell=False, stdout=subprocess.PIPE)
    result = process.communicate()

    #Check Ping Results
    if 'min/avg/max/stddev' in result[0]:
      reachable_ip.append(ip)
    else:
      non_reachable_ip.append(ip)
  
  print_table(reachable_ip, non_reachable_ip)

  f.close()
  

def print_table(reachable, non_reachable):
  print '\n++++++++++++++++++++++++++++++'
  print '|' + "{0:^17s} {1:^} {2:^7s} {1:^}".format('IP Address', '|', 'Status')
  print '|------------------+---------|'

  for pingable in reachable:
    print '|' + "{0:^17s} {1:^} {2:^7s} {1:^}".format(pingable, '|', 'Alive')

  print '|------------------+---------|'

  for nonpingable in non_reachable:
    print '|' + "{0:^17s} {1:^} {2:^7s} {1:^}".format(nonpingable, '|', 'Dead')

  print '++++++++++++++++++++++++++++++\n'


def main():
  if len(sys.argv) != 3:
    print 'usage: ./ping.py {--ip_address | --ping} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--ip_address':
    print_ip(filename)
  elif option == '--ping':
    ping_ip(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)


if __name__ == '__main__':
  main()
