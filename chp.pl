my @list;
print ("digite um valor\n");
$n = <>;
chomp($n); 
for (my $i=1; $i<=$n; $i++){
     push(@list,$i); 
}
print ("@list\n");
foreach my $aux ((),@list){
  print("\n");
  print(@list);
  print("\n");    
  my $aux = shift @list;
  print("Elemneto retirado: ".$aux."\n");
}
print("\n".@list."\n");