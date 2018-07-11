<?php

$command = escapeshellcmd('/root/script/pygithub.py');
$output = shell_exec($command);

#echo $output;

?>
