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
        $limit = 100;
        $initial = 2;
        
        while(TRUE)
        {
            $div = 2;
            if($initial > $limit) 
            {
                break;
            }
            while(TRUE)
            {
                if($div > sqrt($initial))
                {
                    echo $initial."  ";
                    break;
                }
                if($initial % $div == 0) 
                {
                    break;
                }
                $div = $div + 1;
            }
            $initial = $initial + 1;
        }
    ?>

        <script src="" async defer></script>
    </body>
</html>