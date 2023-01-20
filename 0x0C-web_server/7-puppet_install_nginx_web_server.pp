# Install and configure nginx

package { 'nginx':
  provider => 'apt',
  ensure   => 'installed',
}

exec { "remove file":
  path    => ['/usr/bin','/usr/sbin','/bin','/sbin'],
  command => "rm -rf /var/www/html/*",
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => "Hello World!",
}

$conf = @("CONFIG")
      server {
	      listen 80 default_server;
	      listen [::]:80 default_server;

          root /var/www/html;

          index index.html index.htm index.nginx-debian.html;

          server_name _;

          location /redirect_me {
       	      return 301 https://www.google.com;
	      }

          location / {
              try_files \$uri \$uri/ =404;
          }
      }
      | CONFIG

file { '/var/www/html/index.html':
  ensure  => present,
  content => $conf,
}

service { 'nginx':
  ensure => running,
  name   => "nginx",
}
