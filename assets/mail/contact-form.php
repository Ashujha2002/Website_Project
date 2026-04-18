<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $to = "office@abentis.es";
    $subject = "New Contact Form Submission from Abentis Consulting SL";
    
    $name = strip_tags(trim($_POST["conName"]));
    $email = filter_var(trim($_POST["conEmail"]), FILTER_SANITIZE_EMAIL);
    $phone = strip_tags(trim($_POST["conPhone"]));
    $service = strip_tags(trim($_POST["conService"]));
    $message = trim($_POST["conMessage"]);

    if (empty($name) || empty($message) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400);
        echo "Please complete the form and try again.";
        exit;
    }

    $email_content = "Name: $name\n";
    $email_content .= "Email: $email\n";
    $email_content .= "Phone: $phone\n";
    $email_content .= "Service Option: $service\n\n";
    $email_content .= "Message:\n$message\n";

    $email_headers = "From: $name <$email>";

    if (mail($to, $subject, $email_content, $email_headers)) {
        http_response_code(200);
        echo "Y"; // Returns Y for success modal in main.js
    } else {
        http_response_code(500);
        echo "Oops! Something went wrong and we couldn't send your message.";
    }
} else {
    http_response_code(403);
    echo "There was a problem with your submission, please try again.";
}
?>