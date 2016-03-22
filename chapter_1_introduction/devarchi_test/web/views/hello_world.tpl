<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Hello World</title>
</head>
<body>
<p>Welcome {{username}}</p>
<ul>
    %for thing in things:
    <li>{{thing}}</li>
    %end
</ul>

<form action="favorite_fruit" method="post">
    <p>What is your favorite fruit?</p>
    <input type="text" name="fruit" size="40" value=""><br>
    <input type="submit" value="Submit">
</form>
</body>
</html>