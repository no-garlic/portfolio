mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"mpetrou74@hotmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\n\
[theme]\n\
base="dark"\n\n\
primaryColor = "darkred"\n\
" > ~/.streamlit/config.toml
