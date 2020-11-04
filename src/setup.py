from subprocess import check_output
from os import chdir, system
from re import search


def main():
  networkServerFile = '/etc/chirpstack-network-server/chirpstack-network-server.toml'
  applicationServerFile = '/etc/chirpstack-application-server/chirpstack-application-server.toml'
  pgHbaFile = '/etc/postgresql/13/main/pg_hba.conf'

  with open(pgHbaFile, 'r') as f:
    content = f.readlines()
    index, line = getIndexAndLine('postgres.+peer', content)
    line = line.replace('peer', 'trust')
    content[index] = line
  with open(pgHbaFile, 'w') as f: f.writelines(content)

  system('chirpstack-network-server configfile > /etc/chirpstack-network-server/chirpstack-network-server.toml')
  with open (networkServerFile, 'r') as f:
    content = f.readlines()

    index, _ = getIndexAndLine('\\bdsn=', content)
    content[index] = 'dsn="postgres://loraserver_ns:dbpassword@localhost/loraserver_ns?sslmode=disable"'

    index, _ = getIndexAndLine('\\bname=', content)
    content[index] = 'name="AU915"'
  with open(networkServerFile, 'w') as f: f.writelines(content)

  with open(applicationServerFile, 'r') as f:
    content = f.readlines()

    index, _ = getIndexAndLine('\\bdsn=', content)
    content[index] = 'dsn="postgres://chirpstack_as:dbpassword@localhost/chirpstack_as?sslmode=disable"'

    jwtSecret = check_output(["openssl", "rand", "-base64", "32"]).decode('utf-8').replace('\n', '')
    index, _ = getIndexAndLine('\\bjwt_secret=', content)
    content[index] = f'jwt_secret="{jwtSecret}"'
  with open(applicationServerFile, 'w') as f: f.writelines(content)

def getIndexAndLine(subStringToSearch, content):
  index, line = filter(lambda content: search(subStringToSearch, content[1]), enumerate(content)).__next__()
  return index, line


if __name__ == '__main__':
  main()