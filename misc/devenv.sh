alias lcon='python3 $LINERDIR/console.py'
alias lgame='python3 $LINERDIR/main.py'
alias setworkingdir='
    echo "what is your liner git working directory?";
    read dir1;
    dir=$(pwd)/$dir1
    echo "export LINERDIR=$dir" >> $HOME/.zshrc;
    echo "export LINERDIR=$dir" >> $HOME/.bashrc;
    echo "export LINERDIR=$dir" >> $HOME/.bash_profile;
    echo "export LINERDIR=$dir" >> $HOME/.profile;
'
alias lgitup='
    if [ $LINERDIR == "" ]; then
        echo "you need to set you working directory first. do setworkingdir in your console after you sourced this file in your bashrc or zshrc or equivalent!";
        exit ;
    fi
    
    echo "commit message? ";
    read commitmsg;
    cd $LINERDIR;

    echo "pushing onto branch $(git rev-parse --abbrev-ref HEAD), control-c if this is incorrect.";
    sleep 5;

    git commit $commitmsg;
    git push;
'