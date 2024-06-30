# manifest kills a process killmenow using the pkill command.
exec { 'kill_killmenow':
  command => '/usr/bin/pkill killmenow',
  path    => '/usr/bin:/bin:/usr/sbin:/sbin',
}
