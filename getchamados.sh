boolean=true
cookie=""
while true
do
    if [ "$boolean" = true ]
    then
        curl -v --cookie $cookie http://example.com | grep "exampleContent" > content.txt;
        echo
        echo '=============================================='
        echo '============ Updated content.txt ============'
        echo '=============================================='
        boolean=false
    else
        curl -v --cookie $cookie http://example.com | grep "exampleContent" > contentaux.txt;
        echo '=============================================='
        echo '========== Updated contentaux.txt ==========='
        echo '=============================================='
        boolean=true
    fi
    sleep 10
done

