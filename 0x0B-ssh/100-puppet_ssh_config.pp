# Configure client to connect to ssh without password

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content =>
"# SSH config file

host = 18.234.107.94
IdentityFile = ~/.ssh/school
PasswordAuthentication = no
"
}
