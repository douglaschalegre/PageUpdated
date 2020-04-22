boolean=true

while true
do
    if [ "$boolean" = true ]
    then
        curl -v --cookie "COOKIE" link | grep "content" > content.txt;
        echo
        echo '=============================================='
        echo '============ Updated content.txt ============'
        echo '=============================================='
        boolean=false
    else
        curl -v --cookie "COOKIE" link | grep "content" > contentaux.txt;
        echo '=============================================='
        echo '========== Updated contentaux.txt ==========='
        echo '=============================================='
        boolean=true
    fi
    sleep 10
done

