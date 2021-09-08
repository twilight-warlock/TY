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
        $day = "1";
        switch ($day) {
            case "1":
                echo "It is Monday!";
                break;
            case "2":
                echo "It is today!";
                break;
            case "3":
                echo "It is Wednesday!";
                break;
            case "4":
                echo "It is Thursday!";
                break;
            case "5":
                echo "It is Friday!";
                break;
            case "6":
                echo "It is Saturday!";
                break;
            case "7":
                echo "It is Sunday!";
                break;
            default:
                echo "Invalid number!";
        }
    ?>

        <script src="" async defer></script>
    </body>
</html>