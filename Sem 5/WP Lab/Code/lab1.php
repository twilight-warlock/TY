<?php
function Palindrome($number){
	$temp = $number;
	$new = 0;
	while (floor($temp)) {
		$d = $temp % 10;
		$new = $new * 10 + $d;
		$temp = $temp/10;
	}
	if ($new == $number){
		return 1;
	}
	else{
		return 0;
	}
}

$original = 1441;
echo "Palindrome Check Program<br>";
if (Palindrome($original)){
	echo "Palindrome";
}
else {
echo "Not a Palindrome";
}

?>
