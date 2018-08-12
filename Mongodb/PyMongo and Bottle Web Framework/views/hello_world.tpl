<!DOCTYPE html>
<html>
<head>
<title>Hello World! </title>
</head>
<body>

<pr>username {{username}}</pr>

<ul>
%for thing in things:
<li> {{thing}} </li>
%end
</ul>

<form action="/favourite_fruit" method="POST">
What is your favourite fruit : <br>
<input type="text" name="fruit_name",value="">
<br>
<input type="submit" value ="Submit">
</form>



</body>
</html>

