<?php

$pid_filename="pid";
$pid = fopen($pid_filename, 'r');
$pid_contents = fread($pid, filesize($pid_filename));
$cmd ="/usr/bin/sudo /bin/kill -9 $pid_contents";
exec($cmd, $output, $ret_var);
//echo "cmd was $cmd.  output:$output. ret_val was $ret_var.";
//print_r($output);
sleep (2);
if($ret_var == 0) {
   $cmd2="python /var/www/html/app.py & ";
   exec($cmd2, $output2, $ret_val2);
  // sleep (5);
   if($ret_val2 == 0) {
        //print_r($output_2);
        fwrite($pid, $output2[0]);
       echo "Python retstarted.";
   } else {
	echo "Failed to restart";
   }
} else {
   echo " Failed to kill - $cmd. $ret_var";
}

fclose($pid);

echo "<br> Hello World";
?>
