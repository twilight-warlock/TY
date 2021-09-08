<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="">
    </head>
    <body>

    <?php
        $num = 15;  
        echo "<h3>Fibonacci series using recursive function:</h3>";  
        echo "\n";  

        function series($num){  
            if($num == 0){  
                return 0;  
            }else if( $num == 1){  
                return 1;  
            }  else {  
                return (series($num-1) + series($num-2));  
            }   
        }  

        for ($i = 0; $i < $num; $i++){  
            echo series($i);  
            echo "\n"; 
        } 
    ?>

        <script src="" async defer></script>
    </body>
</html>