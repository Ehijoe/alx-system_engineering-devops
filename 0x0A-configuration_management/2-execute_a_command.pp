# Kill the process killmenow

exec { 'killmenow':
  command => ['pkill', 'killmenow']
}
