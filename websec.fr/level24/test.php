#!/usr/bin/php
<?php

$data = base64_encode("<?php echo 1; ?>");
file_put_contents("php://filter/convert.base64-decode/resource=test1.php", $data);

?>
