<?php
    $action=$_GET['action'];    
    // ini_set("display_errors", "off");
    // require_once "../data.php";
    $username = $_POST['username'];
    $password = $_POST['password'];
    $select = $connect -> prepare("SELECT username,password FORM member WHERE username = :us AND password = :pw");
    $select -> execute(array(':us' => $username,':pw' => $password));
    $result = $select -> fetch(PDO::FETCH_ASSOC) ;
       if ($result['username']==$username&&$result['password']==$password) {
            session_start();
            $_SESSION['member'] = $result;
            header("location:./?error=登入成功");
      }
       elseif ($result['password']!=$password||$result['username']!=$username) {
            header("location:./?error=帳密錯誤");
    }
?>