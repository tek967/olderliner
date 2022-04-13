alias lcon='python3 $(pwd)/console.py'
alias lgame='python3 $(pwd)/main.py'
alias setworkingdir='
    echo "what is your liner git working directory?";
    read dir;
    echo "export LINERDIR=$dir" >> .zshrc;
    echo "export LINERDIR=$dir" >> .bashrc;
    echo "export LINERDIR=$dir" >> .bash_profile;
    echo "export LINERDIR=$dir" >> .profile;
'
alias lgitup='
    if [ $LINERDIR == "" ]; then
        echo "you need to set you working directory first. do setworkingdir in your console after you sourced this file in your bashrc or zshrc or equivalent!";
        exit ;
    
    echo "commit message? ";
    read commitmsg;
    cd $LINERDIR;

    echo "pushing onto branch $(git rev-parse --abbrev-ref HEAD), control-c if this is incorrect.";
    sleep 5;

    git commit $commitmsg;
    git push;
'