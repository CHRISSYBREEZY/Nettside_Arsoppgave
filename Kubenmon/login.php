<?php
session_start();

if (isset($_POST['login'])) {
  $username = $_POST['username'];
  $password = $_POST['password'];

  // connect to MySQL database
  $conn = mysqli_connect('localhos', 'yourusername', 'yourpassword', 'yourdatabasename');

  // query the database to check if the user exists and the password is correct
  $query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
  $result = mysqli_query($conn, $query);

  if (mysqli_num_rows($result) == 1) {
    // set session variables and redirect to the home page
    $_SESSION['username'] = $username;
    header('Location: home.php');
    exit();
  } else {

    // display an error message
    $error = "Invalid username or password";
  }
}
?>

