<?php
session_start();
error_reporting(E_ALL);
ini_set('display_errors', '1');
$db_hostname = "127.0.0.1";
$db_username = "root";
$db_password = "";
$db_name = "user_details";

$conn = mysqli_connect($db_hostname, $db_username, $db_password, $db_name);
if (!$conn) {
    echo "error" . mysqli_connect_error();
    exit;
}

$name = $_POST['NAME'];
$email = $_POST['EMAIL'];
$password = $_POST['Password'];

$sql = "INSERT INTO `details_new` (`NAME`, `EMAIL`, `Password`) VALUES('$name','$email','$password')";

$result = mysqli_query($conn, $sql);

if (!$result) {
    echo "error:" . mysqli_error($conn);
    exit;
}

echo "Redirecting...";
header("Location: index1.html");
exit;
?>