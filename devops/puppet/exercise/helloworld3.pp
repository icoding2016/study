# create a hello word file in /var which need sudo privilege
file {'/var':
  ensure => directory,
}
#file {'/var/puppet':
#  ensure => directory,
#  mode => '0755',
#}
file {'/var/helloword2.txt':
  ensure => file,
  mode => '0755',
  content => "Hello World, with creating directory!\n",
  require => File['/var'],
}
