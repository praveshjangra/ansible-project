import os 
import testinfra.utils.ansible_runner 
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(   
             os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')  

"""Role testing files using testinfra."""
users = ['centos','jenkins']
def test_hosts_file(host):
 """Validate /etc/hosts file."""
 f = host.file("/etc/hosts")
 assert f.exists
 assert f.user == "root"
 assert f.group == "root"
def test_centos_user_exist(host):
 """Vlidate if centos user exist"""
 u = host.user("centos")
 assert u.name == "centos"
def test_jenkins_user_exist(host):
 """Vlidate if jenkins user exist"""
 u = host.user("jenkins")
 assert u.name == "jenkins"
def test_ssh_directory_exists(host):
 """Validate that .ssh directory exists"""
 for user in users:
  d=host.file('/home/'+user+'/.ssh')
  assert d.exists
  assert d.is_directory
  assert d.user == user
  assert d.group == user
  assert d.mode == 0o700
def test_authorized_keys_exists(host):
 """Validate that authorized keys exists"""
 for user in users:
  d=host.file('/home/'+user+'/.ssh/authorized_keys')
  assert d.exists
  assert d.user == user
  assert d.group == user
  assert d.mode == 0o600
def test_id_rsa_keys_exists(host):
 """Validate that public key exists"""
 for user in users:
  d=host.file('/home/'+user+'/.ssh/id_rsa.pub')
  assert d.exists
  assert d.user == user
  assert d.group == user
  assert d.mode == 0o644
def test_id_rsa_private_keys_exists(host):
 """Validate that private key exists"""
 for user in users:
  d=host.file('/home/'+user+'/.ssh/id_rsa')
  assert d.exists
  assert d.user == user
  assert d.group == user
  assert d.mode == 0o600
def test_bitbucket_config_exists(host):
 """Validate that bitbucket config exists"""
 for user in users:
  d=host.file('/home/'+user+'/.ssh/config')
  assert d.exists
  assert d.user == user
  assert d.group == user
  assert d.mode == 0o644
def test_bitbucket_config_exists(host):
 """Validate that bitbucket key exists"""
 for user in users:
  d=host.file('/home/'+user+'/.ssh/id_rsa_bitbucket')
  assert d.exists
  assert d.user == user
  assert d.group == user
  assert d.mode == 0o400
def test_packge_installed(host):
 
  pkg = host.package('httpd')
  assert pkg.is_installed

