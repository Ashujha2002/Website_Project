<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $to = "office@abentis.es";
    $subject = "New Newsletter Subscription from Abentis Consulting SL";
    
    $email = filter_var(trim($_POST["s_email"]), FILTER_SANITIZE_EMAIL);

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400);
        echo "Please provide a valid email address.";
        exit;
    }

    $email_content = "New subscriber: $email\n";
    $email_headers = "From: Newsletter <$email>";

    if (mail($to, $subject, $email_content, $email_headers)) {
        http_response_code(200);
        // Redirect back to home with success message or just show success
        header("Location: ../../index.html?status=success");
        echo "Thank you for subscribing!";
    } else {
        http_response_code(500);
        echo "Oops! Something went wrong.";
    }
} else {
    http_response_code(403);
    echo "Access denied.";
}
?>
