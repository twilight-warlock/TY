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

    <form method="post">
        <input type="number" name="salary" value="" placeholder="Enter basic salary"/>
        <input type="submit" name="submit" value="Submit"/>
    </form>
    <?php
        if(isset($_POST['submit']))
        {
            $basic_salary = floatval($_POST['salary']);
            if ($basic_salary == 0){
                echo "Enter value first";
                return 0;
            }
            $dcut = 0.04 * $basic_salary;
            $income_tax = 0.12 * $basic_salary;
            $gross_salary = $basic_salary - $dcut - $income_tax;
            echo "Basic Salary : ".$basic_salary."/- <br>";
            echo "Dividend Cut: " .$dcut."/-<br>";
            echo "Income Tax : " .$income_tax ."/-<br>";
            echo "Gross Salary : " .$gross_salary*12 ."/-";
        }
    ?>

        <script src="" async defer></script>
    </body>
</html>