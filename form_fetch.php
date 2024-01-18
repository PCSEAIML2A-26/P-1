<?php
$db_hostname = "localhost: 4306";
$db_username = "root";
$db_password = "";
$db_name = "user_details";

$conn = mysqli_connect($db_hostname, $db_username, $db_password, $db_name);
if (!$conn) {
    echo "error" . mysqli_connect_error();
    exit;
}
$sql = "SELECT *FROM details_new";

$result = mysqli_query($conn, $sql);
if (!$result) {
    echo "error:" . mysqli_error($conn);
    exit;
}
mysqli_close($conn);
?>