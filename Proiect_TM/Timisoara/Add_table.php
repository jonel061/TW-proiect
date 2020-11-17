<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "timisoara";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}



// sql to create table 
$sql1 = "CREATE TABLE if NOT EXISTS users (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
`username` VARCHAR(30) NOT NULL,
email VARCHAR(50),
`password` varchar(100) NOT NULL
)";

if ($conn->query($sql1) === TRUE) {
    echo "Table users created successfully";
} else {
    echo "Error creating table: " . $conn->error;
}

$sql2 = "CREATE TABLE if NOT EXISTS Nationalitatea (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
`name` VARCHAR(30) NOT NULL,
`gender` VARCHAR(30) NOT NULL,
`nationality` VARCHAR(30) NOT NULL)"; 

if ($conn->query($sql2) === TRUE) {
    echo "Table users created successfully 2";
} else {
    echo "Error creating table: " . $conn->error;
}


$conn->close();
?>