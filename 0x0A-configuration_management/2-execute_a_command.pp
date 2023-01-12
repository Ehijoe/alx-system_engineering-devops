# Kill the process killmenow

exec { 'killmenow':
  command => ['/bin/pkill', 'killmenow']
}
