# Install prerequisites

To use virtualenv to manage dependencies, first setup a virtualenv environment:

    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

To stop the virtualenv

    deactivate

## jupyter themes

My default theme for notebooks:

    jt -t grade3 -nfs 14 -altp -tfs 14 -fs 14 -ofs 14 -dfs 14 -cellw 100% -T
