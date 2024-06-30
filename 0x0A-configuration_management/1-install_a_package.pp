# A manifest to install flask framwork via pip3 package management
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
