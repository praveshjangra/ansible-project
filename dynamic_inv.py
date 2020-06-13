#!/usr/bin/python 
import sys
import json
try: 
    import boto3
except Exception as e:
     print(e)
     print("Please install boto3")
     sys.exit(1)
def get_hosts(ec2_ob,kv):
    f = {"Name":"tag:type", "Values":[kv]}
    hosts=[]
    for each_in  in ec2_ob.instances.filter(Filters=[f]):
        hosts.append(each_in.public_ip_address)
    return hosts
def main():
  ec2_ob=boto3.resource('ec2')
  db_groups=get_hosts(ec2_ob,'db')
  all_groups= {'db' : db_groups}
  print(json.dumps(all_groups))
  return None
if __name__=="__main__":
    main()