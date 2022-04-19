exec { 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config':
  command => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => '/usr/local/bin/:/bin/',
}

exec { 'echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config':
  command => 'echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  path    => '/usr/local/bin/:/bin/',
}