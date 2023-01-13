# Configure client to connect to ssh without password

file { '/etc/ssh/ssh_config':
  path    => '/etc/ssh/ssh_config',
  content =>
"# SSH config file

host = 18.234.107.94
IdentityFile = ~/.ssh/school
PasswordAuthentication = no
",
  mode    => '0777',
}
