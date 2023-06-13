<head>
    <meta charset="">
    <link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>


    <form action="process_form.php" method="POST">
        <!-- Form elements will be added here -->
        <label for="navn">Brukernavn: </label>
        <input type="text" id="brukernavn" name="brukernavn" required><br>

        <label for="passord">Passord: </label>
        <input type="password" id="passord" name="passord"> <br> <br>

        <input type="submit" value="submit">
    </form>
</body>

<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve the submitted form data
    $username = $_POST['brukernavn'];
    $password = $_POST['passord'];

    // Database
    $hostname = '10.2.2.133';
    $db_username = 'root';
    $db_password = '';
    $db_name = 'kubemon';

    $conn = new mysqli($hostname, $db_username, $db_password, $db_name);

    // Check for connection errors
    if ($mysqli->connect_error) {
        die('Connection failed: ' . $mysqli->connect_error);
    }

    // Perform login validation
    $query = "SELECT * FROM brukere WHERE brukernavn = '$username' AND password = '$password'";
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