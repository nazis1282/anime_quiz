<?php
header('Content-Type: application/json');

include('config.php'); // Include the database connection file

// API endpoint to get a random question with answers
if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['getQuestion'])) {
    $sql = "SELECT * FROM questions ORDER BY RAND() LIMIT 1";
    $result = $conn->query($sql);

    if ($result) {
        if ($result->num_rows > 0) {
            $row = $result->fetch_assoc();

            $response = [
                'question' => $row['Question'],
                'answer' => $row['Correct Response'],
                'wrong_answer1' => $row['Wrong Response 1'],
                'wrong_answer2' => $row['Wrong Response 2'],
                'wrong_answer3' => $row['Wrong Response 3']
            ];

            echo json_encode($response);
        } else {
            header('HTTP/1.1 404 Not Found');
            echo json_encode(array('message' => 'No valid questions found.'));
        }
    } else {
        echo json_encode(array('error' => 'Database query error: ' . mysqli_error($conn)));
    }

    $conn->close(); // Close the connection explicitly
} else {
    echo json_encode(array('error' => 'Invalid request.'));
}
