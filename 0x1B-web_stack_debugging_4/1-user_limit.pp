# Increase file limit
exec { 'increase_soft_limit':
  command => "/bin/sed -i 's/hard nofile 5/hard nofile 5000/' /etc/security/limits.conf"
}

exec { 'increase_hard_limit':
  command => "/bin/sed -i 's/soft nofile 4/soft nofile 4000/' /etc/security/limits.conf"
}
