<?php
$judul = $_POST['title'];
$isi   = $_['body'];

$json = ['judul'=>$judul, 'isi'=>$isi];
echo json_encode($json);
?>