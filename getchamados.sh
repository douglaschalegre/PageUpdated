boolean=true

while true
do
    if [ "$boolean" = true ]
    then
        curl -v --cookie "IF PAGE HAVE COOKI PUT HERE" [https://example.com/] | grep "[What you want to track]" > content.txt;
        echo
        echo '=============================================='
        echo '============ Updated content.txt ============'
        echo '=============================================='
        boolean=false
    else
        curl -v --cookie "IF PAGE HAVE COOKI PUT HERE" [https://example.com/] | grep "[What you want to track]" > contentaux.txt;
        echo '=============================================='
        echo '========== Updated contentaux.txt ==========='
        echo '=============================================='
        boolean=true
    fi
    sleep 10
done

