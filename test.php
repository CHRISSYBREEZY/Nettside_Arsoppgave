<?php
    //Databasetilkobling, med databaseplassering, brukernavn, passord og databasenavn 
    $tilkobling = new mysqli("10.2.2.133","root","superpappa321","kubemon");
?>
<?php
    //Sjekker og viser om det er feil med tilkoblingen til databasen
    if ($tilkobling->connect_errno)
        echo ("Failed to connect to MySQL: 
         (" . $tilkobling->connect_errno . ")
         " . $tilkobling->connect_error);

    //Sjekker og viser om det er noe feil med spørringen som kjøres mot databasen
    if (mysqli_errno($tilkobling))
        echo ("Error in query, " . $sql . ",  execution, MySQL returns: 
         (" . $tilkobling->errno . ")
         " . $tilkobling->error );
?>

    <form action="" method="POST" > <input type="hidden" name="command" value="insert"> <tr>
    <td>
    <input type="text" name = "brukernavn" value = "" style="background-color : #d1d1d1;"> 
    </td>
    <td>
    <input type="text" name = "passord" value = "" style="background-color : #d1d1d1;"> 
    </td><td><input type="submit" value="Ny"> </td></tr></form>
</table>
