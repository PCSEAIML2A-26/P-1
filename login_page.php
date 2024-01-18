<?php
session_start();

$db_hostname = "127.0.0.1:4306";
$db_username = "root";
$db_password = "";
$db_name = "user_details";

$conn = mysqli_connect($db_hostname, $db_username, $db_password, $db_name);
if (!$conn) {
    echo "error" . mysqli_connect_error();
    exit;
}

$name = $_POST['email'];
$password = $_POST['Password'];

$sql = "SELECT * FROM details_new WHERE email='$name' AND Password='$password'";

$result = mysqli_query($conn, $sql);

if (!$result) {
    echo "error:" . mysqli_error($conn);
    exit;
}

$row = mysqli_fetch_assoc($result);

if ($row) {
    $_SESSION['email'] = $row['email'];
    setcookie("email", $row['email'], time() + 3600);
    echo "Hello " . $row['email'] . "<br/>";
    header("Location: index1.html");
    exit;
} else {
    echo "Login failed<br/>";
}

mysqli_close($conn);
?>