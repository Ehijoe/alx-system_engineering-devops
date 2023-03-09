# Increase file limit
exec { 'increase_limit':
  command => "/bin/sed -i 's/15/1500/' /etc/default/nginx"
}

exec { 'restart_nginx':
  command => '/usr/sbin/service nginx restart'
}
