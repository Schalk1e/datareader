DIR=$PWD

ANSI_RED='\033[0;31m'
ANSI_GREEN='\033[0;32m'
ANSI_RESET='\033[0m'

lint() {
    failed=0
    isort -c "$@" || failed=1
    black --check -l79 "$@" || failed=1
    return $failed
}

fmt() {
    isort "$@" && black -l79 "$@"
}

if [ ! -d $DIR/src ] 
then
    echo "Please run from root :)"
    exit 1
fi

lint src
result=$?

if [ $result = 0 ]; then
    echo "${ANSI_GREEN}Lint passed!${ANSI_RESET}"
else
    echo "${ANSI_RED}Lint failed!${ANSI_RESET}"
    echo "Would you like to format the codebase? (Y/N)"
    read user_prompt
    if [ $user_prompt = Y ]; then
        echo "Reformatting..."
        fmt src
    fi
fi

echo "Would you like to run flake8? (Y/N)"
read flake_prompt
if [ $flake_prompt = Y ]; then
    echo "Running flake8 checks... Action if necessary:"
    flake8 . --count --show-source --statistics --config=.flake8.cfg
fi

exit $result
