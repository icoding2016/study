file {'/tmp':
  ensure => directory,
}
file {'/tmp/puppet':
  ensure => directory,
  # mode => '0755',
}
file {'/tmp/puppet/helloword2.txt':
  ensure => file,
  mode => '0755',
  content => "Hello World, with creating directory!\n",
  require => File['/tmp/puppet'],
}

