boolean=true
cookie=""
green='\033[0;32m'
nc='\033[0m'
while true
do
    if [ "$boolean" = true ]
    then
        curl -v --cookie $cookie http://example.com | grep "example\|example2" > content.txt;
        echo -e ${green}'[+]'${nc} 'Content.txt updated'
        boolean=false
    else
        curl -v --cookie $cookie http://example.com | grep "example\|example2" > contentaux.txt;
        echo -e ${green}'[+]'${nc} 'ContentAux.txt updated'
        boolean=true
    fi
    sleep 30
done

