# Configure client to connect to ssh without password

include stdlib

file { '/etc/ssh/config':
  ensure => present,
}

file_line { 'Ensure no password is accepted':
  path => '/etc/ssh/config',
  line => 'PasswordAuthentication = no',
}

file_line { 'Ensure no password is accepted':
  path => '/etc/ssh/config',
  line => 'IdentityFile = ~/.ssh/school',
}
