boolean=true
cookie="glpi_f8245b57fcd351174c77313b7def86a1=tqn5sns2gadniajhhai8udsep2; glpi_f8245b57fcd351174c77313b7def86a1_rememberme=%5B%225652%22%2C%22%242y%2410%24pAHPGciGQb9hv%5C%2FXolKPIfubSwz0UzQu9MDUI3mGt3HtCeNhKlPT5y%22%5D"
while true
do
    if [ "$boolean" = true ]
    then
        curl -v --cookie $cookie http://portalti.tjal.jus.br/glpi/front/ticket.php | grep "id='Ticket" > content.txt;
        echo
        echo '=============================================='
        echo '============ Updated content.txt ============'
        echo '=============================================='
        boolean=false
    else
        curl -v --cookie $cookie http://portalti.tjal.jus.br/glpi/front/ticket.php | grep "id='Ticket" > contentaux.txt;
        echo '=============================================='
        echo '========== Updated contentaux.txt ==========='
        echo '=============================================='
        boolean=true
    fi
    sleep 10
done

