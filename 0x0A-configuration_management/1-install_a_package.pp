# A manifest to install flask framwork on Werzbeug and python3.8.1 via pip3 package management
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

package { 'python3.8.10':
  ensure   => '3.8.10',
  provider => 'pip3',
}

