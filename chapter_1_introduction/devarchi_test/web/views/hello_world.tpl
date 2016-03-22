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
</body>
</html>