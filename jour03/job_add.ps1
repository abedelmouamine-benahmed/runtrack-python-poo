Param(
[int]$nb_job 
)

For($i=1;$i -le $nb_job;$i++)
{   
 If($i -lt 10){  
  	New-item job0$i}
 else{
 	New-item job$i}

}
  