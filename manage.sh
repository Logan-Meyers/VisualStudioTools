#!/run/current-system/sw/bin/bash

# repo manager
function repo_manager {
    while true; do
        clear
        echo "Choose an option:"
        echo "s.  show status -- \`git status\`"
        echo "fp. fetch and pull -- \`git fetch && git pull\`"
        echo "a.  add all changes -- \`git add .\`"
        echo "c.  commit changes -- \`git commit -m \$MSG\`"
        echo "p.  push changes -- \`git push\`"
        echo "q.  exit git manager"
        echo -n "> "

        read git_choice

        echo

        case $git_choice in
            s)
                git status
                ;;
            fp)
                git fetch && git pull
                ;;
            a)
                git add .
                ;;
            c)
                echo "Please enter what you want your commit message to be:"
                echo -n "> "

                read comm_msg

                git commit -m "$comm_msg"
                ;;
            p)
                git push
                ;;
            q)
                break
                ;;
            *)
                echo "Invalid option!"
                ;;
        esac

        _pause
    done
}

# config manager


# profile manager


# pause func
function _pause {
    read -p "Press enter to continue..."
}

# main loop
while true; do
    clear
    echo "===== Nix Manager ====="
    echo
    echo "Choose an option:"
    echo "1. Manage this git repo"
    echo "2. Manage system configuration files"
    echo "3. Manage system profiles"
    echo "4. exit"
    echo -n "> "

    read choice

    case $choice in
        1)
            repo_manager
            _pause
            ;;
        2)
            ;;
        4)
            echo "Exiting..."
            break
            ;;
        *)
            echo "Invalid option!"
            ;;
    esac
done

