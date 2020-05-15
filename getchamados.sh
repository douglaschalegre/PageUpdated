boolean=true
cookie=""
while true
do
    if [ "$boolean" = true ]
    then
        curl -v --cookie $cookie http://example.com | grep "example\|example2" > content.txt;
        echo '[+] Content.txt updated'
        boolean=false
    else
        curl -v --cookie $cookie http://example.com | grep "example\|example2" > contentaux.txt;
        echo '[+] ContentAux.txt updated'
        boolean=true
    fi
    sleep 30
done

