<?php

include 'database.php';

$python_output = "";
for($i = 0; $i < 50;$i++) {
    $code = sha1(rand());
    $database->query("INSERT INTO vouchers (`code`) VALUES ('$code')");
    $python_output .= "\"$code\", ";
}

$database->close();

echo $python_output;