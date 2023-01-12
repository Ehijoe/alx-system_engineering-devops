# Kill the process killmenow

exec { 'pkill killmenow':
  command => '/usr/bin/pkill killmenow',
}
