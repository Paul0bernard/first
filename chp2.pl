print ("digite um valor\n");
$n = <>;
chomp($n); 

for (my $i=1; $i<=$n; $i++){
     push(@list,$i); 
}     

print(scalar("o tamnaho do vetor é: ".@list."\n"));

my $i = scalar @list;
foreach(1..$i)
{
        print("\n");  
 	print(@list);
  	print("\n");
  	my $aux = shift @list;	
  	print("Elemento retirado: ".$aux."\n");	
}