<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve the submitted form data
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Database connection details
    $hostname = '10.2.2.133';
    $db_username = 'root';  // Default username for XAMPP is 'root'
    $db_password = '';      // Default password for XAMPP is empty
    $db_name = 'kubemon';  // Name of the database you created

    // Create a new MySQLi object and establish the database connection
    $mysqli = new mysqli($hostname, $db_username, $db_password, $db_name);

    // Check for connection errors
    if ($mysqli->connect_error) {
        die('Connection failed: ' . $mysqli->connect_error);
    }

    // Perform login validation
    $query = "SELECT * FROM test1 WHERE username = '$username' AND password = '$password'";
    $result = $mysqli->query($query);

    if ($result->num_rows == 1) {
        // Login successful
        echo 'Login successful!';
    } else {
        // Invalid credentials
        echo 'Invalid credentials. Please try again.';
    }

    // Close the database connection
    $mysqli->close();
}
?>
