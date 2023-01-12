# Install flask 2.1.0 with pip3

package { 'flask':
  provider => 'pip3',
  ensure   => '2.1.0',
}
