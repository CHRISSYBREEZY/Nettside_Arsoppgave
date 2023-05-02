<?php

#koble til 
$servername = "127.0.0.1";
$username = "";
$password = "yourpassword";
$dbname = "users";

 

$conn = new mysqli($servername, $username, $password, $dbname);

 

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if user submitted the login form
if (isset($_POST['login'])) {

    // Retrieve login form data
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Query database for user with matching email and password
    $sql = "SELECT * FROM users WHERE email = '$email' AND password = '$password'";
    $result = $conn->query($sql);

    // Check if a user was found
    if ($result->num_rows == 1) {
        // User was found, redirect to dashboard
        header("Location: dashboard.php");
        exit();
    } else {
        // User was not found, display error message
        $error = "Invalid email or password";
    }
}


