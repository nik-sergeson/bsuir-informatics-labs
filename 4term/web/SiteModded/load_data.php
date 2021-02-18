<?php
session_start();

if($_POST['page']) {
	$page = intval($_POST['page']);
	if($page < 1) $page = 10;
	
	$currentPage = $page;
	$page -= 1;
	$perPage = 10;
	$previousButton = true;
	$nextButton = true;
	$firstButton = true;
	$lastButton = true;
	$start = $page * $perPage;
	$visiblePagesCount = 5;
	
	include("db.php");

	$data = "SELECT id, name, descr FROM artists LIMIT $start, $perPage";
	$data = mysql_query($data) or die('MySql Error' . mysql_error());
	$tag = "";
	while ($row = mysql_fetch_array($data)) {
            $name = htmlspecialchars($row['name']);
            $descr = htmlspecialchars($row['descr']);
            $tag .= "<tr><td class=\"itemid\">" . $row['id'] . "</td><td class=\"itemname\">" . $name . "</td><td class=\"itemy\">" . $descr . "</td></tr>";
	} 
	$tag = "<div><table class=\"itemtable\"" . $tag . "</table></div>";

	//$pagesNumber = "SELECT COUNT(*) AS count FROM atrists";
	$resultPagesNumber = mysql_query("SELECT COUNT(*) AS count FROM artists");
	$row = mysql_fetch_array($resultPagesNumber);
	$count = $row['count'];
	$pagesCount = ceil($count / $perPage);
	
	$firstPage = 1;
	if ($pagesCount > $visiblePagesCount)
		$lastPage = $visiblePagesCount;
	else
		$lastPage = $pagesCount;
		
	if ($lastPage + $currentPage - 1 <= $pagesCount) {
		$firstPage = $firstPage + $currentPage - 1;
		$lastPage = $lastPage + $currentPage - 1;
	} else {
		$firstPage = $pagesCount - $visiblePagesCount + 1;
		$lastPage = $pagesCount;
	}	
	
	$tag .= "<div class='numbs'><ul class='group'>";	

	if ($previousButton && $currentPage > 1) {
		$pre = $currentPage - 1;
		$tag .= "<li p='$pre' class='active'>&lt;</li>";
	} else if ($previousButton) {
		$tag .= "<li class='inactive'>&lt;</li>";
	}
	
	for ($i = $firstPage; $i <= $lastPage; ++$i) {

		if ($currentPage == $i)
			$tag .= "<li p='$i' class='active current'>{$i}</li>";
		else
			$tag .= "<li p='$i' class='active'>{$i}</li>";
	}
	
	if ($nextButton && $currentPage < $pagesCount) {
		$nex = $currentPage + 1;
		$tag .= "<li p='$nex' class='active'>&gt;</li>";
	} else if ($nextButton) {
		$tag .= "<li class='inactive'>&gt;</li>";
	}	
	$tag .= "</ul></div>";
	echo $tag;
} 
?>
