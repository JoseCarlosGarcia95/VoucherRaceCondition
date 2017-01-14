<?php

include 'database.php';

if(empty($_GET['voucher']))
    die();
$voucher = $_GET['voucher'];

$query = $database->query("SELECT null FROM `vouchers` WHERE `code` = '" . $database->real_escape_string($voucher) . "'");

if($query->num_rows == 0) {
    die("ERROR!");
}

$database->query("DELETE FROM `vouchers` WHERE `code` = '" . $database->real_escape_string($voucher) . "'");

echo "OK";