# udp_receiver.pl

use IO::Socket::INET;

# Turn on System variable for Buffering output
$| = 1;

$port= 5000;

# Create a a new socket
$socket=new IO::Socket::INET->new(LocalPort=>$port,Proto=>'udp');

print "\nUDP Server: waiting for client on port $port ...";
$cnt= 1;

while(1)
{
	$socket->recv($buffer,1024);
	$n= length $buffer;
	$peer_address = $socket->peerhost();
	$peer_port = $socket->peerport();

	print "\n $cnt ($peer_address:$peer_port) received : $n bytes\n";

	$buffer =~ s/(.)/sprintf("%02X ",ord($1))/eg;
	print $buffer;

	$cnt++;
}


